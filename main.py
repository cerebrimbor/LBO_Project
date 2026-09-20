import numpy as np

from regime_engine import simulate_economic_path
from sources_uses import sponsor_equity
from operating_forecast import simulate_operating_forecast
from debt_schedule import simulate_debt_schedule
from assumptions import holding_period


def simulate_lbo(seed=None, rng=None):

    # Create one RNG for the entire simulation
    if rng is None:
        rng = np.random.default_rng(seed)

    # 1. Economic path
    economic_path = simulate_economic_path(
        holding_period,
        rng=rng
    )

    # 2. Operating forecast
    revenues, ebitdas = simulate_operating_forecast(
        economic_path
    )

    # 3. Debt schedule
    debt_schedule = simulate_debt_schedule(
        economic_path,
        revenues,
        ebitdas
    )

    # 4. Exit valuation
    final_ebitda = ebitdas[-1]
    final_debt = debt_schedule[-1]["ending_debt"]

    exit_multiple = economic_path[-1]["valuation_multiple"]

    exit_enterprise_value = (
        final_ebitda * exit_multiple
    )

    raw_exit_equity = (
        exit_enterprise_value - final_debt
    )

    # 5. Distress / loss handling
    if raw_exit_equity <= 0:

        exit_equity = 0
        distressed = True
        status = "DISTRESSED"

    else:

        exit_equity = raw_exit_equity
        distressed = False

        moic = exit_equity / sponsor_equity

        if moic < 1.0:
            status = "LOSS"
        else:
            status = "PROFITABLE"

    # 6. Returns
    moic = exit_equity / sponsor_equity

    if moic <= 0:
        irr = -1.0
    else:
        irr = moic ** (1 / holding_period) - 1

    return {
        "economic_path": economic_path,
        "revenues": revenues,
        "ebitdas": ebitdas,
        "debt_schedule": debt_schedule,
        "exit_equity": exit_equity,
        "raw_exit_equity": raw_exit_equity,
        "distressed": distressed,
        "status": status,
        "moic": moic,
        "irr": irr
    }


if __name__ == "__main__":

    result = simulate_lbo()

    print("ECONOMIC PATH")

    for year in result["economic_path"]:

        print(
            f"Y{year['year']}: "
            f"{year['regime']:<10} "
            f"Growth={year['revenue_growth']:.1%} "
            f"Margin={year['ebitda_margin']:.1%} "
            f"Rate={year['interest_rate']:.1%} "
            f"Multiple={year['valuation_multiple']:.2f}x"
        )

    print()

    print(f"MOIC: {result['moic']:.2f}x")
    print(f"IRR: {result['irr']:.2%}")
    print(f"Status: {result['status']}")