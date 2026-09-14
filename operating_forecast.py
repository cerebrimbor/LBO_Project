from assumptions import revenue, ebitda


def simulate_operating_forecast(economic_path):

    revenues = [revenue]
    ebitdas = [ebitda]

    for year in economic_path:

        growth = year["revenue_growth"]
        margin = year["ebitda_margin"]

        next_revenue = revenues[-1] * (1 + growth)
        next_ebitda = next_revenue * margin

        revenues.append(next_revenue)
        ebitdas.append(next_ebitda)

    return revenues, ebitdas