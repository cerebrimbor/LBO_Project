from regime_engine import simulate_economic_path
from sources_uses import sponsor_equity
from operating_forecast import revenues, ebitdas
from debt_schedule import debt_schedule

def simulate_lbo():
    economic_path = simulate_economic_path(5)
    final_ebitda = ebitdas[-1]
    final_debt = debt_schedule[-1]["ending_debt"]
    exit_equity = exit_equity_value(final_ebitda, final_debt, economic_path[-1]["valuation_multiple"])
    moic = exit_equity / sponsor_equity
    irr = moic ** (1 / 5) - 1
    
    return {
        "economic_path": economic_path,
        "exit_equity": exit_equity,
        "moic": moic,
        "irr": irr
    }

# Run one simulation
result = simulate_lbo()

print("MOIC:", result["moic"])
print("IRR:", result["irr"])        
    


#def format_money(value):
#    if abs(value) >= 1000:
#        return f"${value / 1000:.2f}B"
#    return f"${value:.2f}M"

#Acquisition
#print("\n" + "=" * 60)
#print("LBO MODEL")

#print("\n1. ACQUISITION")
#print(f"Enterprise Value: {format_money(enterprise_value)}")
#print(f"Equity Value:     {format_money(equity_value)}")

#Sources and uses
#print("\n2. SOURCES & USES")

#print("\nUSES")
#print(f"Purchase Equity:  {format_money(purchase_equity)}")
#print(f"Refinance Debt:   {format_money(refinance_debt)}")
#print(f"Transaction Fees: {format_money(transaction_fees)}")
#print(f"Total Uses:       {format_money(total_uses)}")

#print("\nSOURCES")
#print(f"New Debt:         {format_money(new_debt)}")
#print(f"Sponsor Equity:   {format_money(sponsor_equity)}")
#print(f"Total Sources:    {format_money(total_sources)}")

#print(f"\nModel Check:      {format_money(sources_uses_check)}")

#Operatng forecast
#print("\n3. OPERATING FORECAST")
#print(f"{'Year':<10}{'Revenue':>15}{'EBITDA':>15}")

#for year in range(1, len(revenues)):
   # print(
        #f"Y{year:<9}"
        #f"{format_money(revenues[year]):>15}"
        #f"{format_money(ebitdas[year]):>15}"
    #)

#Debt schedule
#print("\n4. DEBT SCHEDULE")

#print(
   # f"{'Year':<6}"
    #f"{'Beginning Debt':>18}"
    #f"{'Interest':>15}"
   # f"{'FCF':>15}"
   # f"{'Repayment':>18}"
    #f"{'Ending Debt':>18}"
#)

#print("-" * 90)

#for row in debt_schedule:
   # print(
     #   f"Y{row['year']:<5}"
      #  f"{format_money(row['beginning_debt']):>18}"
       # f"{format_money(row['interest']):>15}"
       # f"{format_money(row['free_cash_flow']):>15}"
       # f"{format_money(row['debt_repayment']):>18}"
       # f"{format_money(row['ending_debt']):>18}"
    #)

#Exit valuation and returns
#print("\n5. EXIT VALUATION & RETURNS")

#print(f"Year 5 EBITDA:          {format_money(year_5_ebitda)}")
#print(f"Remaining Debt:         {format_money(remaining_debt)}")
#print(f"Exit Enterprise Value:  {format_money(exit_enterprise_value)}")
#print(f"Exit Equity Value:      {format_money(exit_equity_value)}")

#print("\nPE RETURNS")
#print(f"MOIC:                    {moic:.2f}x")
#print(f"IRR:                     {irr:.2%}")

#print("\n" + "=" * 60)
#print("END")
    