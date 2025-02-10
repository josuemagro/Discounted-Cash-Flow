import yfinance as yf
import functions
import math

stock = yf.Ticker("AAPL") #Edit This

risk_free_asset = 0.1325 #Edit This

market_return = 0.114 #Edit This


income_statement = stock.financials
balance_sheet = stock.balance_sheet


beta = stock.info.get("beta")

cost_of_equity = functions.calculate_cost_of_equity(risk_free_asset, beta, market_return)

interest_expense = functions.get_most_recent_value(income_statement, "Interest Expense")

total_debt = functions.get_most_recent_value(balance_sheet, "Total Debt")

income_tax_expense = functions.get_most_recent_value(income_statement, "Tax Provision")

income_before_tax = functions.get_most_recent_value(income_statement, "Pretax Income")

cost_of_debt = functions.calculate_cost_of_debt(interest_expense, total_debt)

tax_rate = functions.effective_tax_rate(income_tax_expense, income_before_tax)

cost_of_debt_after_tax = functions.cost_of_debt_after_tax(cost_of_debt, tax_rate)

total_debt = functions.get_most_recent_value(balance_sheet, "Total Debt")

market_cap = stock.info.get("marketCap")

sum_of_total_debt_and_market_cap = total_debt + market_cap

total_debt_percent = total_debt / sum_of_total_debt_and_market_cap

market_cap_percent = market_cap / sum_of_total_debt_and_market_cap

wacc = cost_of_debt * total_debt_percent + cost_of_equity * market_cap_percent

variables_to_check = {
    "Interest Expense": interest_expense,
    "Total Debt": total_debt,
    "Tax provision": income_tax_expense,
    "Pretax Income": income_before_tax,
    "Total Debt": total_debt,
    "Market Cap": market_cap,
}

print(f"Ticker: {stock.info["symbol"]}\n")


check_data = functions.check_and_display_variables(variables_to_check)

if check_data == True:
    print(f"Cost of Equity: {cost_of_equity:.2f}%")

    print(f"Cost of Debt after Tax: {cost_of_debt_after_tax:.2f}%")

    print(f"WACC: {wacc:.2f}%") 
else:
    print("Sorry, Some recent data might be missing from Yahoo Finance.")
    print("You could manually change the value of the variable")






