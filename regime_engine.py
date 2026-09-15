import numpy as np

from ou_engine import simulate_ou_step


#Economic regimes
regimes = [
    "Expansion",
    "Normal",
    "Slowdown",
    "Recession"
]


#Markov transition matrix
transition_matrix = [
    [0.70, 0.20, 0.08, 0.02],  # Expansion
    [0.15, 0.65, 0.15, 0.05],  # Normal
    [0.05, 0.20, 0.60, 0.15],  # Slowdown
    [0.02, 0.08, 0.25, 0.65]   # Recession
]


#Economic parameters
regime_parameters = {

    "Expansion": {
        "revenue_growth": 0.10,
        "ebitda_margin": 0.22,
        "interest_rate": 0.07,

        "ou_kappa": 1.50,
        "ou_mean": 12.0,
        "ou_sigma": 0.80
    },

    "Normal": {
        "revenue_growth": 0.08,
        "ebitda_margin": 0.20,
        "interest_rate": 0.08,

        "ou_kappa": 1.50,
        "ou_mean": 10.0,
        "ou_sigma": 0.60
    },

    "Slowdown": {
        "revenue_growth": 0.03,
        "ebitda_margin": 0.19,
        "interest_rate": 0.09,

        "ou_kappa": 1.50,
        "ou_mean": 8.0,
        "ou_sigma": 0.50
    },

    "Recession": {
        "revenue_growth": -0.05,
        "ebitda_margin": 0.16,
        "interest_rate": 0.11,

        "ou_kappa": 1.50,
        "ou_mean": 6.0,
        "ou_sigma": 0.40
    }
}


def next_regime(current_regime, rng):

    current_index = regimes.index(current_regime)

    probabilities = transition_matrix[current_index]

    next_index = rng.choice(
        len(regimes),
        p=probabilities
    )

    return regimes[next_index]


def get_regime_parameters(regime):

    return regime_parameters[regime]


def simulate_economic_path(
    years,
    starting_regime="Normal",
    starting_multiple=10.0,
    rng=None
):

    if rng is None:
        rng = np.random.default_rng()

    current_regime = starting_regime
    current_multiple = starting_multiple

    economic_path = []

    for year in range(1, years + 1):

        parameters = get_regime_parameters(
            current_regime
        )

        # OU valuation multiple
        current_multiple = simulate_ou_step(
            current_value=current_multiple,
            kappa=parameters["ou_kappa"],
            long_run_mean=parameters["ou_mean"],
            sigma=parameters["ou_sigma"],
            rng=rng,
            dt=1.0
        )

        economic_path.append({
            "year": year,
            "regime": current_regime,
            "revenue_growth":
                parameters["revenue_growth"],
            "ebitda_margin":
                parameters["ebitda_margin"],
            "interest_rate":
                parameters["interest_rate"],
            "valuation_multiple":
                current_multiple
        })

        current_regime = next_regime(
            current_regime,
            rng
        )

    return economic_path