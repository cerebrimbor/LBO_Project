from assumptions import holding_period
from operating_forecast import ebitdas
from debt_schedule import debt_schedule
from sources_uses import sponsor_equity
from regime_engine import economic_path

#Exit valuation
year_5_ebitda = ebitdas[-1]
remaining_debt = debt_schedule[-1]["ending_debt"]
exit_multiple = economic_path[-1]["valuation_multiple"]
exit_enterprise_value = year_5_ebitda * exit_multiple
exit_equity_value = exit_enterprise_value - remaining_debt

#MOIC
moic = exit_equity_value / sponsor_equity
#IRR
irr = (moic ** (1/holding_period)) - 1

        