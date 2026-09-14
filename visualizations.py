import os
import numpy as np
import matplotlib.pyplot as plt
from monte_carlo import run_monte_carlo
from regime_engine import regimes, transition_matrix

# Output directory
FIGURE_DIR = "figures"

os.makedirs(
    FIGURE_DIR,
    exist_ok=True
)


results = run_monte_carlo(1000)

all_results = results["all_results"]

moics = results["moic_results"]


#MOIC distributions
plt.figure(figsize=(12, 7))

plt.hist(
    moics,
    bins=40,
    density=True
)

plt.axvline(
    1.0,
    linestyle="--",
    linewidth=2,
    label="1.0x Loss Threshold"
)

plt.axvline(
    results["moic_p50"],
    linestyle="-",
    linewidth=2,
    label=f"Median = {results['moic_p50']:.2f}x"
)

plt.xlabel("MOIC")
plt.ylabel("Density")

plt.title(
    "Stochastic LBO Return Distribution\n"
    "1,000 Regime-Switching + OU Simulations"
)

plt.legend()

plt.tight_layout()

plt.savefig(
    os.path.join(
        FIGURE_DIR,
        "moic_distribution.png"
    ),
    dpi=300,
    bbox_inches="tight"
)

plt.show()


#Debt leveraging

debt_paths = []
for result in all_results:

    debt_path = [
        row["ending_debt"]
        for row in result["debt_schedule"]
    ]

    debt_paths.append(debt_path)
    
debt_paths = np.array(debt_paths)

years = np.arange(
    1,
    debt_paths.shape[1] + 1
)


debt_p5 = np.percentile(
    debt_paths,
    5,
    axis=0
)

debt_p25 = np.percentile(
    debt_paths,
    25,
    axis=0
)

debt_p50 = np.percentile(
    debt_paths,
    50,
    axis=0
)

debt_p75 = np.percentile(
    debt_paths,
    75,
    axis=0
)

debt_p95 = np.percentile(
    debt_paths,
    95,
    axis=0
)


plt.figure(figsize=(12, 7))

plt.fill_between(
    years,
    debt_p5,
    debt_p95,
    alpha=0.15,
    label="5th–95th percentile"
)

plt.fill_between(
    years,
    debt_p25,
    debt_p75,
    alpha=0.25,
    label="25th–75th percentile"
)

plt.plot(
    years,
    debt_p50,
    linewidth=2.5,
    label="Median Debt"
)

plt.xlabel("Year")
plt.ylabel("Ending Debt ($M)")

plt.title(
    "Stochastic LBO Deleveraging\n"
    "Debt Distribution Across Economic Paths"
)

plt.legend()

plt.tight_layout()

plt.savefig(
    os.path.join(
        FIGURE_DIR,
        "debt_fan_chart.png"
    ),
    dpi=300,
    bbox_inches="tight"
)

plt.show()


#OU
plt.figure(figsize=(12, 7))

number_of_paths = min(
    100,
    len(all_results)
)

for result in all_results[:number_of_paths]:

    multiple_path = [
        year["valuation_multiple"]
        for year in result["economic_path"]
    ]

    years = [
        year["year"]
        for year in result["economic_path"]
    ]

    plt.plot(
        years,
        multiple_path,
        alpha=0.08
    )


plt.xlabel("Year")
plt.ylabel("Valuation Multiple (x)")

plt.title(
    "OU Valuation Multiple Paths\n"
    "Conditional on Markov Economic Regimes"
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        FIGURE_DIR,
        "ou_multiple_paths.png"
    ),
    dpi=300,
    bbox_inches="tight"
)

plt.show()


#Markov transition matrix

transition_array = np.array(
    transition_matrix
)


plt.figure(figsize=(8, 7))

plt.imshow(
    transition_array,
    aspect="auto"
)

plt.xticks(
    range(len(regimes)),
    regimes,
    rotation=20
)

plt.yticks(
    range(len(regimes)),
    regimes
)

plt.xlabel("Next Regime")
plt.ylabel("Current Regime")

plt.title(
    "Economic Regime Transition Matrix"
)


# Add probability labels
for i in range(len(regimes)):

    for j in range(len(regimes)):

        probability = transition_array[i, j]

        plt.text(
            j,
            i,
            f"{probability:.0%}",
            ha="center",
            va="center"
        )


plt.colorbar(
    label="Transition Probability"
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        FIGURE_DIR,
        "regime_heatmap.png"
    ),
    dpi=300,
    bbox_inches="tight"
)

plt.show()


print()
print("FIGURES GENERATED")
print("-----------------")
print(
    f"Saved to: "
    f"{os.path.abspath(FIGURE_DIR)}"
)