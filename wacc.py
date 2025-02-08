import yfinance as yf

stock = yf.Ticker("VBBR3.SA")

risk_free_asset = 0.1325

market_return = 0.114

beta = stock.info.get("beta")

def calculate_cost_of_equity(risk_free_asset, beta, market_return):
    ke = (risk_free_asset + beta * (market_return - risk_free_asset)) * 100
    return ke

cost_of_equity = calculate_cost_of_equity(risk_free_asset, beta, market_return)

print(f"Cost of Equity: {cost_of_equity:.2f}%")

income_statement = stock.financials
balance_sheet = stock.balance_sheet

def get_most_recent_value(data, metric_name):
    if metric_name in data.index:
        return data.loc[metric_name].iloc[0]
    return None

interest_expense = get_most_recent_value(income_statement, "Interest Expense")

total_debt = get_most_recent_value(balance_sheet, "Total Debt")

income_tax_expense = get_most_recent_value(income_statement, "Tax Provision")




