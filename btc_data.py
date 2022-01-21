import yfinance as yf
import pandas as pd

def get_stock_data(period, interval):
    btc = yf.download(tickers='BTC-USD', period = period, interval = interval)
    btc.reset_index(inplace=True)
    btc = btc[['Datetime', 'Adj Close', 'Volume']]
    btc['Hours_tmp'] = btc.loc[:,'Datetime']
    times_stock_d = pd.to_datetime(btc.Datetime)
    times_stock_h = pd.to_datetime(btc.Hours_tmp)
    btc['Date'] = times_stock_d.dt.date
    btc['Hours'] = times_stock_h.dt.hour
    btc['Minutes'] = times_stock_h.dt.minute
    df_stock = btc[['Date', 'Hours', 'Minutes','Adj Close']]
    df_stock.to_csv('btc_data.csv')
    return df_stock

