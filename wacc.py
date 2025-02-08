import yfinance as yf
import functions

stock = yf.Ticker("VBBR3.SA")

risk_free_asset = 0.1325

market_return = 0.114

beta = stock.info.get("beta")

cost_of_equity = functions.calculate_cost_of_equity(risk_free_asset, beta, market_return)

print(f"Cost of Equity: {cost_of_equity:.2f}%")

income_statement = stock.financials
balance_sheet = stock.balance_sheet

interest_expense = functions.get_most_recent_value(income_statement, "Interest Expense")

total_debt = functions.get_most_recent_value(balance_sheet, "Total Debt")

income_tax_expense = functions.get_most_recent_value(income_statement, "Tax Provision")

income_before_tax = functions.get_most_recent_value(income_statement, "Pretax Income")

cost_of_debt = functions.calculate_cost_of_debt(interest_expense, total_debt)

tax_rate = functions.effective_tax_rate(income_tax_expense, income_before_tax)

cost_of_debt_after_tax = functions.cost_of_debt_after_tax(cost_of_debt, tax_rate)

print(f"Cost of Debt after Tax: {cost_of_debt_after_tax:.2f}%")



