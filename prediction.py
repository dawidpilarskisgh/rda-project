import pickle
import pandas as pd
import numpy as np
import datetime

now = datetime.datetime.now()
prediction_date = (now + datetime.timedelta(minutes=(60 - now.minute))).strftime("%Y-%m-%d %H:%M")

def prepare_data(data_to_predict, ver):
    df_data = data_to_predict
    if ver == 'NLTK':
        x_columns = ['Negative_nltk','Neutral_nltk','Positive_nltk','len', 'Likes', 'RTs', 0]
    else:
        x_columns = ['sentiment_text_blob', 'len', 'Likes', 'RTs', 0]
    y_columns = [5,10,15,20,25,30,35,40,45,50,55]
    X = np.array(df_data[x_columns])
    Y = np.array(df_data[y_columns])
    return X

def load_model(filename):
    reg  = pickle.load(open(filename, 'rb'))
    return reg

def make_linear_prediction(data_to_predict, ver):
    X_test = prepare_data(data_to_predict, ver)
    file = 'LinearRegression_model_'+ver+'.sav'
    linear_model = load_model(file)

    y_predict = linear_model.predict(X_test)
    df_y_predict = pd.DataFrame(y_predict)

    df_y_predict['Model type'] = ['Linear Regression']
    df_y_predict['Prediction time'] = [prediction_date]
    df_y_predict['Sentiment type'] = [ver]

    return df_y_predict


def make_RandomForestRegressor_prediction(data_to_predict, ver):
    X_test  = prepare_data(data_to_predict, ver)
    file = 'RandomForestRegressor_model_' + ver + '.sav'
    rf_model = load_model(file)
    y_predict = rf_model.predict(X_test)
    df_y_predict = pd.DataFrame(y_predict)

    df_y_predict['Model type'] = ['Random Forest Regressor']
    df_y_predict['Prediction time'] = [prediction_date]
    df_y_predict['Sentiment type'] = [ver]

    return df_y_predict

def predict(data_to_predict):
    first_solution = data_to_predict[['Date','Hours','len','Likes','RTs','sentiment_text_blob',0,5,10,15,20,25,30,35,40,45,50,55]]
    second_solution = data_to_predict[['Date','Hours','len','Likes','RTs','Negative_nltk','Neutral_nltk','Positive_nltk',0,5,10,15,20,25,30,35,40,45,50,55]]
    linear_pred = make_linear_prediction(first_solution, 'TextBlob')
    rfr = make_RandomForestRegressor_prediction(first_solution, 'TextBlob')
    df_all = linear_pred.append(rfr)

    linear_pred2 = make_linear_prediction(second_solution, 'NLTK')
    rfr2 = make_RandomForestRegressor_prediction(second_solution, 'NLTK')
    df_all2 = linear_pred2.append(rfr2)

    result = df_all.append(df_all2)
    result.to_csv('prediction_data.csv')
    return result

