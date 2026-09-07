from assumptions import (revenue,ebitda,existing_debt,cash,entry_multiple)
#Enterprise Value
enterprise_value = ebitda * entry_multiple

#Equity value
equity_value = enterprise_value - existing_debt + cash