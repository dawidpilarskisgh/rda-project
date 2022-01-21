import pickle
from math import sqrt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import datetime

now = datetime.datetime.now()
prediction_date = (now + datetime.timedelta(minutes=(60 - now.minute))).strftime("%Y-%m-%d %H:%M")

FILE = 'data/data_to_prediction_model_v2.csv'
time_column = [prediction_date for i in range(14)]
lr = ['Linear Regression' for x in range(14)]
rf = ['Random Forest Regressor' for z in range(14)]
type_pred = ['Prediction' for y in range(14)]
type_real = ['Real data' for m in range(14)]


def prepare_data(ver):
    df_data = pd.read_csv(FILE)
    if ver == 'NLTK':
        x_columns = ['Negative_nltk', 'Neutral_nltk', 'Positive_nltk', 'len', 'Likes', 'RTs', '0']
    else:
        x_columns = ['sentiment_text_blob', 'len', 'Likes', 'RTs', '0']
    y_columns = ['5','10','15','20','25','30','35','40','45','50','55']
    X = np.array(df_data[x_columns])
    Y = np.array(df_data[y_columns])
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state = 0)
    return X_train, X_test, y_train, y_test

def create_linear_model(X, Y, ver):
    reg = LinearRegression()
    reg.fit(X, Y)
    filename = 'LinearRegression_model_'+ver+'.sav'
    pickle.dump(reg, open(filename, 'wb'))
    return reg

def make_linear_prediction(ver):
    X_train, X_test, y_train, y_test = prepare_data(ver)
    linear_model = create_linear_model(X_train, y_train, ver)
    y_predict = linear_model.predict(X_test)
    df_y_predict = pd.DataFrame(y_predict)
    df_y_test = pd.DataFrame(y_test)
    df_y_predict['Model type'] = lr
    df_y_predict['Prediction time'] = time_column
    df_y_predict['Type'] = type_pred
    df_y_test['Type'] = type_real
    result = pd.concat([df_y_predict, df_y_test], axis=1)
    check_model(y_test, y_predict, 'Linear_Regression')
    print('Linear regression: R score = ' , linear_model.score(X_train, y_train))
    return result

def create_RandomForestRegressor(X,Y, ver):
    rf = RandomForestRegressor()
    rf.fit(X, Y)
    filename = 'RandomForestRegressor_model_'+ver+'.sav'
    pickle.dump(rf, open(filename, 'wb'))
    return rf


def make_RandomForestRegressor_prediction(ver):
    X_train, X_test, y_train, y_test = prepare_data(ver)
    rf_model = create_RandomForestRegressor(X_train, y_train, ver)
    y_predict = rf_model.predict(X_test)
    df_y_predict = pd.DataFrame(y_predict)
    df_y_test = pd.DataFrame(y_test)
    df_y_predict['Model type'] = lr
    df_y_predict['Prediction time'] = time_column
    df_y_predict['Type'] = type_pred
    df_y_test['Type'] = type_real
    result = pd.concat([df_y_predict, df_y_test], axis=1)
    check_model(y_test, y_predict, 'RandomForest')
    print('RandomForestRegressor: R score = ' ,rf_model.score(X_test, y_test))
    return result

def check_model(actual, predict, model):
    print(model, 'r2 score:',r2_score(actual, predict))
    print(model, 'MAE:',mean_absolute_error(actual, predict))
    print(model, 'MSE:', mean_squared_error(actual, predict))
    print(model, 'rmse :', sqrt(mean_squared_error(actual, predict)))


def predict():
    linear_pred = make_linear_prediction()
    rfr = make_RandomForestRegressor_prediction()
    df_all = linear_pred.append(rfr)
    df_all.to_csv('prediction_data.csv')
    return df_all


def create_models(ver):
    make_linear_prediction(ver)
    make_RandomForestRegressor_prediction(ver)

version = ['TextBlob', 'NLTK']

for ver in version:
    create_models(ver)

