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
current_regime = "Normal"

def next_regime(current_regime):
    current_index = regimes.index(current_regime)
    probabilities = transition_matrix[current_index]
    return random.choices(regimes,weights=probabilities,k=1)[0]

print("REGIME SIMULATION")

for year in range(1, 6):

    print(f"Year {year}: {current_regime}")

    current_regime = next_regime(current_regime)    