# LBO model
def format_money(value):
    if abs(value) >= 1000:
        return f"${value / 1000:.2f}B"
    else:
        return f"${value:.2f}M"

#target company financials
revenue= 1000	#$ million
ebitda = 200	#$ million
existing_debt = 300	#$ million
cash = 50       #$ million

#Acquisition assumption
entry_multiple = 10

#Enterprise Value
enterprise_value = ebitda * entry_multiple

#Equity value
equity_value = enterprise_value - existing_debt + cash
 
#Uses
transaction_fees = 50
purchase_equity = equity_value
refinance_debt = existing_debt
total_uses = (
    purchase_equity
    + refinance_debt
    + transaction_fees
)

#Sources
debt_multiple = 5
new_debt = ebitda * debt_multiple
sponsor_equity = total_uses - new_debt
total_sources = new_debt + sponsor_equity

sources_uses_check = total_sources - total_uses
print("LBO ACQUISITION")
print(f"Revenue: {format_money(revenue)}")
print(f"EBITDA: {format_money(ebitda)}")
print(f"Entry Multiple: {entry_multiple}x")
print("-------------------------------------")
print(f"Enterprise Value: {format_money(enterprise_value)}")
print(f"Equity Value: {format_money(equity_value)}")

print("\n Sources and uses")

print("\nUSES")
print(f"Purchase Equity:  {format_money(purchase_equity)}")
print(f"Refinance Debt:   {format_money(refinance_debt)}")
print(f"Transaction Fees: {format_money(transaction_fees)}")
print("-------------------------------------")
print(f"Total Uses:       {format_money(total_uses)}")

print("\nSOURCES")
print(f"New Debt:         {format_money(new_debt)}")
print(f"Sponsor Equity:   {format_money(sponsor_equity)}")
print("-------------------------------------")
print(f"Total Sources:    {format_money(total_sources)}")

print("\nMODEL CHECK")
print(f"Sources - Uses:   {format_money(sources_uses_check)}")