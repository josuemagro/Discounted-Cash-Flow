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


def interest_expense():
    income_statement = stock.financials

    if "Interest Expense" in income_statement.index:
        interest_expense_recent = income_statement.loc["Interest Expense"].iloc[0]
        recent_year = income_statement.columns[0].strftime("%Y") 
        return interest_expense_recent
    else:
        print("Interest Expense não encontrado na demonstração de resultados.")

