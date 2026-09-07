from assumptions import (ebitda,existing_debt,transaction_fees,debt_multiple)
from acquisition import equity_value

#Uses
purchase_equity = equity_value
refinance_debt = existing_debt
total_uses = (purchase_equity + refinance_debt + transaction_fees)

#Sources
new_debt = ebitda * debt_multiple
sponsor_equity = total_uses - new_debt
total_sources = new_debt + sponsor_equity

sources_uses_check = total_sources - total_uses