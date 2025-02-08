import yfinance as yf

stock = yf.Ticker("AAPL")

risk_free_asset = 0.1325

market_return = 0.114

beta = stock.info.get("beta")

