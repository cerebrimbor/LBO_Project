#Dynamic Debt Schedule
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
holding_period = 5

#Debt Schedule
beginning_debt = initial_debt
debt_schedule = []

for year in range(1, holding_period + 1):

    revenue = revenues[year]
    ebitda = ebitdas[year]
    
    interest = beginning_debt * interest_rate

    taxable_income = ebitda - interest
    taxes = taxable_income * tax_rate

    capex = revenue * capex_percent_revenue

    change_nwc = revenue * nwc_percent_revenue

    free_cash_flow = (ebitda- interest- taxes- capex- change_nwc)

    debt_repayment = min(free_cash_flow, beginning_debt)

    ending_debt = beginning_debt - debt_repayment

    # Store results
    debt_schedule.append({
        "year": year,
        "beginning_debt": beginning_debt,
        "interest": interest,
        "free_cash_flow": free_cash_flow,
        "debt_repayment": debt_repayment,
        "ending_debt": ending_debt
    })

    # Next year beginning debt
    beginning_debt = ending_debt
 
print("Debt Schedule")

print(
    f"{'Year':<8}"
    f"{'Beginning Debt':>20}"
    f"{'Interest':>15}"
    f"{'FCF':>15}"
    f"{'Debt Repayment':>20}"
    f"{'Ending Debt':>18}"
)

for row in debt_schedule:

    print(
        f"Y{row['year']:<7}"
        f"{format_money(row['beginning_debt']):>20}"
        f"{format_money(row['interest']):>15}"
        f"{format_money(row['free_cash_flow']):>15}"
        f"{format_money(row['debt_repayment']):>20}"
        f"{format_money(row['ending_debt']):>18}"
    )