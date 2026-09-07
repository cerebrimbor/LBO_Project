from assumptions import (revenue,ebitda,holding_period,revenue_growth,ebitda_margin)

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
