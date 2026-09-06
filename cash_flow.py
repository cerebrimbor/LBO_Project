#Cash Flow
def format_money(value):
    if abs(value) >= 1000:
        return f"${value / 1000:.2f}B"
    else:
        return f"${value:.2f}M"

#Operating Forecast Inputs
revenues = [1000,1080,1166.4,1259.712,1360.48896,1469.3280768]
ebitdas = [200,216,233.28,251.9424,272.097792,293.86561536]

#Cash flow assumptions
tax_rate = 0.25 
capex_percent_revenue = 0.03
nwc_percent_revenue = 0.01
initial_debt = 1000
interest_rate = 0.08       

#Cash flow calculation
free_cash_flows = []
for year in range(1, 6):

    revenue = revenues[year]
    ebitda = ebitdas[year]

    # Interest expense
    interest = initial_debt * interest_rate

    # Tax calculation
    taxable_income = ebitda - interest
    taxes = taxable_income * tax_rate

    # Capital expenditure
    capex = revenue * capex_percent_revenue

    # Change in Net Working Capital
    change_nwc = revenue * nwc_percent_revenue

    # Free Cash Flow
    free_cash_flow = (ebitda- interest- taxes- capex- change_nwc)

    free_cash_flows.append(free_cash_flow)
    


print("CASH FLOW")    

print(
    f"{'Year':<8}"
    f"{'EBITDA':>15}"
    f"{'Interest':>15}"
    f"{'Taxes':>15}"
    f"{'CapEx':>15}"
    f"{'ΔNWC':>15}"
    f"{'FCF':>15}"
)

for year in range(1, 6):

    revenue = revenues[year]
    ebitda = ebitdas[year]

    interest = initial_debt * interest_rate
    taxes = (ebitda - interest) * tax_rate
    capex = revenue * capex_percent_revenue
    change_nwc = revenue * nwc_percent_revenue

    fcf = free_cash_flows[year - 1]

    print(
        f"Y{year:<7}"
        f"{format_money(ebitda):>15}"
        f"{format_money(interest):>15}"
        f"{format_money(taxes):>15}"
        f"{format_money(capex):>15}"
        f"{format_money(change_nwc):>15}"
        f"{format_money(fcf):>15}"
    )