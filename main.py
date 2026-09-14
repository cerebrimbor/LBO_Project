from regime_engine import simulate_economic_path
from sources_uses import sponsor_equity
from operating_forecast import simulate_operating_forecast
from debt_schedule import simulate_debt_schedule
from assumptions import holding_period


def simulate_lbo():

    # 1. Economic path
    economic_path = simulate_economic_path(holding_period)

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

    exit_equity = (
        exit_enterprise_value - final_debt
    )

    # 5. Returns
    moic = exit_equity / sponsor_equity

    irr = moic ** (1 / holding_period) - 1

    return {
        "economic_path": economic_path,
        "revenues": revenues,
        "ebitdas": ebitdas,
        "debt_schedule": debt_schedule,
        "exit_equity": exit_equity,
        "moic": moic,
        "irr": irr
    }


# Run one simulation
result = simulate_lbo()

print("MOIC:", result["moic"])
print("IRR:", result["irr"])