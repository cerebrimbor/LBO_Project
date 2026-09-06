#Exit Valuation and Returns
def format_money(value):
    if abs(value) >= 1000:
        return f"${value / 1000:.2f}B"
    else:
        return f"${value:.2f}M"

#Exit assumptions
initial_sponsor_equity = 1100
remaining_debt = 559.48     # Remaining debt from debt schedule


exit_multiple = 10
holding_period = 5
year_5_ebitda = 293.86561536  # Year 5 EBITDA from operating forecast


#Exit valuation
exit_enterprise_value = year_5_ebitda * exit_multiple
exit_equity_value = exit_enterprise_value - remaining_debt

#Returns

#Multiple on Invested Capital
moic = exit_equity_value / initial_sponsor_equity

#Internal Rate of Return
irr = (moic ** (1/holding_period)) - 1

print("EXIT VALUATION & RETURNS")

print("\nEXIT ASSUMPTIONS")
print(f"Year 5 EBITDA:       {format_money(year_5_ebitda)}")
print(f"Exit Multiple:       {exit_multiple}x")
print(f"Remaining Debt:      {format_money(remaining_debt)}")

print("\nEXIT VALUATION")
print(f"Exit Enterprise Value: {format_money(exit_enterprise_value)}")
print(f"Exit Equity Value:     {format_money(exit_equity_value)}")

print("\nPE RETURNS")
print(f"Initial Investment:  {format_money(initial_sponsor_equity)}")
print(f"MOIC:                {moic:.2f}x")
print(f"IRR:                 {irr:.2%}")
        