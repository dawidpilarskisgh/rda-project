import pickle
import pandas as pd
import numpy as np
import datetime

now = datetime.datetime.now()
prediction_date = (now + datetime.timedelta(minutes=(60 - now.minute))).strftime("%Y-%m-%d %H:%M")

def prepare_data(data_to_predict):
    df_data = data_to_predict
    x_columns = ['sentiment','len', 'Likes', 'RTs', 0]
    y_columns = [5,10,15,20,25,30,35,40,45,50,55]
    X = np.array(df_data[x_columns])
    Y = np.array(df_data[y_columns])
    return X

def load_model(filename):
    reg  = pickle.load(open(filename, 'rb'))
    return reg

def make_linear_prediction(data_to_predict):
    X_test = prepare_data(data_to_predict)
    linear_model = load_model('LinearRegression_model.sav')

    y_predict = linear_model.predict(X_test)
    df_y_predict = pd.DataFrame(y_predict)

    df_y_predict['Model type'] = ['Linear Regression']
    df_y_predict['Prediction time'] = [prediction_date]

    return df_y_predict


def make_RandomForestRegressor_prediction(data_to_predict):
    X_test  = prepare_data(data_to_predict)
    rf_model = load_model('RandomForestRegressor_model.sav')
    y_predict = rf_model.predict(X_test)
    df_y_predict = pd.DataFrame(y_predict)

    df_y_predict['Model type'] = ['Random Forest Regressor']
    df_y_predict['Prediction time'] = [prediction_date]

    return df_y_predict

def predict(data_to_predict):
    linear_pred = make_linear_prediction(data_to_predict)
    rfr = make_RandomForestRegressor_prediction(data_to_predict)
    df_all = linear_pred.append(rfr)
    df_all.to_csv('prediction_data.csv')
    return df_all

