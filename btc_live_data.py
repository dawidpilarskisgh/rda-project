import yfinance as yf

period = '2h'
interval = '1h'

btc = yf.download(tickers='BTC-USD', period = period, interval = interval)

#print(btc)
btc.to_csv('btc_data.csv')
