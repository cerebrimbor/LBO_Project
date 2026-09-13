from assumptions import revenue, ebitda
from regime_engine import economic_path

# Operating Forecast

revenues = [revenue]
ebitdas = [ebitda]

for year in economic_path:

    growth = year["revenue_growth"]
    margin = year["ebitda_margin"]

    next_revenue = revenues[-1] * (1 + growth)
    next_ebitda = next_revenue * margin

    revenues.append(next_revenue)
    ebitdas.append(next_ebitda)