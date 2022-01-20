import pandas as pd
pd.options.mode.chained_assignment = None
import datetime

def prepare_data(stock_data, twitter_data):
    df_stock_btc = stock_data #pd.read_csv('data/btc_data.csv')
    df_data = twitter_data #pd.read_csv('data/all_data_bitcoin.csv')

    df_tmp = df_data[['Date', 'len', 'Likes', 'RTs', 'sentiment']]
    df_tmp['Hours'] = df_tmp.loc[:,'Date']
    times_d = pd.to_datetime(df_tmp.Date)
    times_h = pd.to_datetime(df_tmp.Hours)  + datetime.timedelta(hours=1 )
    date = times_d.dt.date
    hours = times_h.dt.hour
    df_groupby_data = df_tmp.groupby([ date, hours]).mean().round(2).reset_index()

    df_stock_tmp = df_stock_btc.pivot(index=['Date', 'Hours'], columns='Minutes', values='Adj Close')
    df_stock_tmp.reset_index(inplace=True)

    df_groupby_data[['Date', 'Hours']] = df_groupby_data[['Date', 'Hours']].astype(str)
    df_stock_tmp[['Date', 'Hours']] = df_stock_tmp[['Date', 'Hours']].astype(str)
    result = pd.merge(df_groupby_data, df_stock_tmp, how='left',on = ['Date', 'Hours'])
    result.to_csv('data_to_prediction_model.csv')
    return result
