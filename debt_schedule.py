from assumptions import (holding_period,interest_rate,tax_rate,capex_percent_revenue,nwc_percent_revenue)
from operating_forecast import revenues, ebitdas
from sources_uses import new_debt

#Debt Schedule
beginning_debt = new_debt
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
 