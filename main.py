from twitter_data import get_data_from_API
from btc_data import get_stock_data
from data_preparation import prepare_data
from prediction import predict

WORDS_TO_SEARCH = ['bitcoin', 'crypto', 'cryptonews', 'cryptocurrency', 'cryptocurrencies', 'BTC', 'bitmark', 'binance', 'bitbay', 'blockchain', 'PaidInBitcoin']
PERIOD_BTC_STOCK = '2h'
INTERVAL_BTC_STOCK = '5m'

## 1st step - download data from TWITTER API since last hour
data_from_twitter = get_data_from_API(WORDS_TO_SEARCH)

## 2nd step - download BTC stock price since last hour
stock_data = get_stock_data(PERIOD_BTC_STOCK, INTERVAL_BTC_STOCK)

## 3rd step - data preparation
prepared_data = prepare_data(stock_data, data_from_twitter)

## 4th - prediction
predicted_data = predict(prepared_data.head(1))
