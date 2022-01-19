from math import sqrt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import datetime

now = datetime.datetime.now()
prediction_date = (now + datetime.timedelta(minutes=(60- now.minute))).strftime("%Y-%m-%d %H:%M")

FILE = 'data_to_prediction_model.csv'

time_column = [prediction_date for i in range(14)]
lr = ['Linear Regression' for x in range(14)]
rf = ['Random Forest Regressor' for z in range(14)]
# print(time_column)
def prepare_data():
    df_data = pd.read_csv(FILE)
    x_columns = ['sentiment','len', 'Likes', 'RTs', '0']
    y_columns = ['5','10','15','20','25','30','35','40','45','50','55']
    X = np.array(df_data[x_columns])
    Y = np.array(df_data[y_columns])
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state = 0)
    return X_train, X_test, y_train, y_test

def create_linear_model(X, Y):
    reg = LinearRegression()
    reg.fit(X, Y)
    return reg

def make_linear_prediction():
    X_train, X_test, y_train, y_test = prepare_data()
    linear_model = create_linear_model(X_train, y_train)
    y_predict = linear_model.predict(X_test)
    #check_model(y_test, y_predict, 'Linear_Regression')
    #print('Linear regression: R score = ' , linear_model.score(X_train, y_train))
    return y_predict

def create_RandomForestRegressor(X,Y):
    rf = RandomForestRegressor()
    rf.fit(X, Y)
    return rf


def make_RandomForestRegressor_prediction():
    X_train, X_test, y_train, y_test = prepare_data()
    rf_model = create_RandomForestRegressor(X_train, y_train)
    y_predict = rf_model.predict(X_test)
   # check_model(y_test, y_predict, 'RandomForest')
    #print('Decision tree: R score = ' , clf_model.score(X_train, y_train))
   # print('RandomForestRegressor: R score = ' ,rf_model.score(X_test, y_test))
    return [y_test, y_predict]

def check_model(actual, predict, model):
    print(model, 'r2 score:',r2_score(actual, predict))
    print(model, 'MAE:',mean_absolute_error(actual, predict))
    print(model, 'MSE:', mean_squared_error(actual, predict))
    print(model, 'rmse :', sqrt(mean_squared_error(actual, predict)))




linear_pred = make_linear_prediction()
rfr = make_RandomForestRegressor_prediction()

print(rfr)
#
# df_lp = pd.DataFrame(linear_pred)
# df_rfr = pd.DataFrame(rfr)
#
# df_lp['Model type'] = lr
# df_lp['Prediction time'] = time_column
#
# df_rfr['Model type'] = rf
# df_rfr['Prediction time'] = time_column
#
#
# df_all = df_lp.append(df_rfr)
#
# df_all.to_csv('prediction_data')
#
# print(df_all)
