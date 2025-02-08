import yfinance as yf

stock = yf.Ticker("VALE3.SA")

risk_free_asset = 0.1325

beta = stock.info.get('beta')
print(f"Beta: {beta}")