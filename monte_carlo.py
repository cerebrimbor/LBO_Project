from main import simulate_lbo

# Monte Carlo settings
mc_sims = 1000

# Store simulation results
moic_results = []
irr_results = []

# Monte Carlo simulation
for m in range(mc_sims):

    result = simulate_lbo()

    moic_results.append(result["moic"])
    irr_results.append(result["irr"])

# Summary stats
average_moic = sum(moic_results) / len(moic_results)
average_irr = sum(irr_results) / len(irr_results)

print("MONTE CARLO RESULTS")
print("-------------------")
print(f"Simulations: {mc_sims}")
print(f"Average MOIC: {average_moic:.2f}x")
print(f"Average IRR: {average_irr:.2%}")