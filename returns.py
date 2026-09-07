#Exit Valuation and Returns
from assumptions import (exit_multiple,holding_period)
from operating_forecast import ebitdas
from debt_schedule import debt_schedule
from sources_uses import sponsor_equity

#Exit valuation
exit_enterprise_value = year_5_ebitda * exit_multiple
exit_equity_value = exit_enterprise_value - remaining_debt

#Returns

#Multiple on Invested Capital
moic = exit_equity_value / initial_sponsor_equity

#Internal Rate of Return
irr = (moic ** (1/holding_period)) - 1

        