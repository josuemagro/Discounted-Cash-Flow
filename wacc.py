import yfinance as yf

stock = yf.Ticker("AAPL")

risk_free_asset = 0.1325

market_return = 0.114

beta = stock.info.get("beta")

def calculate_cost_of_equity(risk_free_asset, beta, market_return):
    ke = (risk_free_asset + beta * (market_return - risk_free_asset)) * 100
    return ke

cost_of_equity = calculate_cost_of_equity(risk_free_asset, beta, market_return)

print(f"Cost of Equity: {cost_of_equity:.2f}%")