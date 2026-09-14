from main import simulate_lbo


# Monte Carlo settings
mc_sims = 1000


def run_monte_carlo(simulation_count=mc_sims):

    # Store complete simulation results
    all_results = []

    # Run simulations
    for _ in range(simulation_count):

        result = simulate_lbo()

        all_results.append(result)

    # Extract MOIC and IRR
    moic_results = [
        result["moic"]
        for result in all_results
    ]

    irr_results = [
        result["irr"]
        for result in all_results
    ]

    # Count distressed cases
    distressed_count = sum(
        result["distressed"]
        for result in all_results
    )

    # Sort results
    sorted_moics = sorted(moic_results)
    sorted_irrs = sorted(irr_results)

    # Average
    average_moic = (
        sum(moic_results)
        / len(moic_results)
    )

    average_irr = (
        sum(irr_results)
        / len(irr_results)
    )

    # Percentile function
    def percentile(values, percentile):

        index = int(
            (percentile / 100)
            * (len(values) - 1)
        )

        return values[index]

    # MOIC percentiles
    moic_p5 = percentile(sorted_moics, 5)
    moic_p25 = percentile(sorted_moics, 25)
    moic_p50 = percentile(sorted_moics, 50)
    moic_p75 = percentile(sorted_moics, 75)
    moic_p95 = percentile(sorted_moics, 95)

    # IRR percentiles
    irr_p5 = percentile(sorted_irrs, 5)
    irr_p25 = percentile(sorted_irrs, 25)
    irr_p50 = percentile(sorted_irrs, 50)
    irr_p75 = percentile(sorted_irrs, 75)
    irr_p95 = percentile(sorted_irrs, 95)

    # Downside probabilities
    moic_below_1 = sum(
        moic < 1.0
        for moic in moic_results
    ) / simulation_count

    irr_below_10 = sum(
        irr < 0.10
        for irr in irr_results
    ) / simulation_count

    distress_probability = (
        distressed_count
        / simulation_count
    )

    return {
        "all_results": all_results,

        "moic_results": moic_results,
        "irr_results": irr_results,

        "average_moic": average_moic,

        "moic_p5": moic_p5,
        "moic_p25": moic_p25,
        "moic_p50": moic_p50,
        "moic_p75": moic_p75,
        "moic_p95": moic_p95,

        "average_irr": average_irr,

        "irr_p5": irr_p5,
        "irr_p25": irr_p25,
        "irr_p50": irr_p50,
        "irr_p75": irr_p75,
        "irr_p95": irr_p95,

        "moic_below_1": moic_below_1,
        "irr_below_10": irr_below_10,
        "distress_probability": distress_probability
    }


# Only print results when this file
# is run directly.

if __name__ == "__main__":

    results = run_monte_carlo()

    print("MONTE CARLO RESULTS")
    print("-------------------")

    print(
        f"Simulations: "
        f"{len(results['all_results'])}"
    )

    print("\nMOIC")

    print(
        f"Average: "
        f"{results['average_moic']:.2f}x"
    )

    print(
        f"5th Percentile: "
        f"{results['moic_p5']:.2f}x"
    )

    print(
        f"25th Percentile: "
        f"{results['moic_p25']:.2f}x"
    )

    print(
        f"Median: "
        f"{results['moic_p50']:.2f}x"
    )

    print(
        f"75th Percentile: "
        f"{results['moic_p75']:.2f}x"
    )

    print(
        f"95th Percentile: "
        f"{results['moic_p95']:.2f}x"
    )

    print("\nIRR")

    print(
        f"Average: "
        f"{results['average_irr']:.2%}"
    )

    print(
        f"5th Percentile: "
        f"{results['irr_p5']:.2%}"
    )

    print(
        f"25th Percentile: "
        f"{results['irr_p25']:.2%}"
    )

    print(
        f"Median: "
        f"{results['irr_p50']:.2%}"
    )

    print(
        f"75th Percentile: "
        f"{results['irr_p75']:.2%}"
    )

    print(
        f"95th Percentile: "
        f"{results['irr_p95']:.2%}"
    )

    print("\nDOWNSIDE RISK")

    print(
        f"P(MOIC < 1.0x): "
        f"{results['moic_below_1']:.2%}"
    )

    print(
        f"P(IRR < 10%): "
        f"{results['irr_below_10']:.2%}"
    )

    print(
        f"P(Distress): "
        f"{results['distress_probability']:.2%}"
    )