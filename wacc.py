import yfinance as yf

stock = yf.Ticker("AAPL")

risk_free_asset = 0.1325

beta = stock.info.get("beta")

