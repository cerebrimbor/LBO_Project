import random
#Economic Regimes
regimes = ["Expansion","Normal","Slowdown","Recession"]

# Markov transition matrix
transition_matrix = [
    [0.70, 0.20, 0.08, 0.02],  # Expansion
    [0.15, 0.65, 0.15, 0.05],  # Normal
    [0.05, 0.20, 0.60, 0.15],  # Slowdown
    [0.02, 0.08, 0.25, 0.65]   # Recession
]

#Addding regime parameters
# Economic parameters for each regime

regime_parameters = {
    "Expansion": {
        "revenue_growth": 0.10,
        "ebitda_margin": 0.22,
        "interest_rate": 0.07,
        "valuation_multiple": 12
    },
    "Normal": {
        "revenue_growth": 0.08,
        "ebitda_margin": 0.20,
        "interest_rate": 0.08,
        "valuation_multiple": 10
    },
    "Slowdown": {
        "revenue_growth": 0.03,
        "ebitda_margin": 0.19,
        "interest_rate": 0.09,
        "valuation_multiple": 8
    },
    "Recession": {
        "revenue_growth": -0.05,
        "ebitda_margin": 0.16,
        "interest_rate": 0.11,
        "valuation_multiple": 6
    }
}    

def next_regime(current_regime):
    current_index = regimes.index(current_regime)
    probabilities = transition_matrix[current_index]
    return random.choices(regimes,weights=probabilities,k=1)[0]

def get_regime_parameters(regime):
    return regime_parameters[regime]

def simulate_economic_path(years, starting_regime="Normal"):
    current_regime = starting_regime
    economic_path = []

    for year in range(1, years + 1):
        parameters = get_regime_parameters(current_regime)
        
        economic_path.append({
            "year": year,
            "regime": current_regime,
            "revenue_growth": parameters["revenue_growth"],
            "ebitda_margin": parameters["ebitda_margin"],
            "interest_rate": parameters["interest_rate"],
            "valuation_multiple": parameters["valuation_multiple"]
        })

        current_regime = next_regime(current_regime)

    return economic_path

economic_path = simulate_economic_path(5)

print("ECONOMIC PATH")
for year in economic_path:
    print(
        f"Y{year['year']}: "
        f"{year['regime']:<10} "
        f"Growth={year['revenue_growth']:.1%} "
        f"Margin={year['ebitda_margin']:.1%} "
        f"Rate={year['interest_rate']:.1%} "
        f"Multiple={year['valuation_multiple']}x"
    )