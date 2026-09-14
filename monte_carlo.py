from main import simulate_lbo

# Monte Carlo settings
mc_sims = 1000

# Store simulation results
moic_results = []
irr_results = []
distressed_count = 0

# Monte Carlo simulation
for m in range(mc_sims):

    result = simulate_lbo()

    moic_results.append(result["moic"])
    irr_results.append(result["irr"])
    
    if result["distressed"]:
        distressed_count += 1

moic_results.sort()
irr_results.sort()

average_moic = sum(moic_results) / len(moic_results)
average_irr = sum(irr_results) / len(irr_results)

def percentile(values, percentile):

    index = int((percentile / 100) * (len(values) - 1))

    return values[index]

# MOIC percentiles
moic_p5 = percentile(moic_results, 5)
moic_p25 = percentile(moic_results, 25)
moic_p50 = percentile(moic_results, 50)
moic_p75 = percentile(moic_results, 75)
moic_p95 = percentile(moic_results, 95)


# IRR percentiles
irr_p5 = percentile(irr_results, 5)
irr_p25 = percentile(irr_results, 25)
irr_p50 = percentile(irr_results, 50)
irr_p75 = percentile(irr_results, 75)
irr_p95 = percentile(irr_results, 95)

# Downside probabilities
moic_below_1 = sum(
    moic < 1.0 for moic in moic_results
) / mc_sims

irr_below_10 = sum(
    irr < 0.10 for irr in irr_results
) / mc_sims


distress_probability = distressed_count / mc_sims

# Output
print("MONTE CARLO RESULTS")
print("-------------------")

print(f"Simulations: {mc_sims}")

print("\nMOIC")
print(f"Average: {average_moic:.2f}x")
print(f"5th Percentile: {moic_p5:.2f}x")
print(f"25th Percentile: {moic_p25:.2f}x")
print(f"Median: {moic_p50:.2f}x")
print(f"75th Percentile: {moic_p75:.2f}x")
print(f"95th Percentile: {moic_p95:.2f}x")

print("\nIRR")
print(f"Average: {average_irr:.2%}")
print(f"5th Percentile: {irr_p5:.2%}")
print(f"25th Percentile: {irr_p25:.2%}")
print(f"Median: {irr_p50:.2%}")
print(f"75th Percentile: {irr_p75:.2%}")
print(f"95th Percentile: {irr_p95:.2%}")

print("\nDOWNSIDE RISK")
print(f"P(MOIC < 1.0x): {moic_below_1:.2%}")
print(f"P(IRR < 10%): {irr_below_10:.2%}")
print(f"P(Distress): {distress_probability:.2%}")