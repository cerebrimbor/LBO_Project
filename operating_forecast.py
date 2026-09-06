revenue = 1000
ebitda = 200

# Forecast Assumptions
holding_period = 5
revenue_growth = 0.08
ebitda_margin = 0.20


# Operating Forecast

revenues = [revenue]
ebitdas = [ebitda]

for year in range(1, holding_period + 1):

    # Revenue growth
    next_revenue = revenues[-1] * (1 + revenue_growth)
    revenues.append(next_revenue)

    # EBITDA calculation
    next_ebitda = next_revenue * ebitda_margin
    ebitdas.append(next_ebitda)

def format_money(value):
    if abs(value) >= 1000:
        return f"${value / 1000:.2f}B"
    else:
        return f"${value:.2f}M"

print("Operating Forecast")

print(
    f"{'Year':<10}"
    f"{'Revenue':>15}"
    f"{'Growth':>12}"
    f"{'EBITDA Margin':>18}"
    f"{'EBITDA':>15}"
)

print("-" * 70)

for year in range(holding_period + 1):

    growth_display = "-"
    if year > 0:
        growth_display = f"{revenue_growth:.1%}"

    print(
        f"Y{year:<9}"
        f"{format_money(revenues[year]):>15}"
        f"{growth_display:>12}"
        f"{ebitda_margin:>17.1%}"
        f"{format_money(ebitdas[year]):>15}"
    )