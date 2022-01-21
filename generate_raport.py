import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('data/prediction_data.csv')

prediction_data = np.array(df.iloc[:, 1:12])
model_type = np.array(df.iloc[:, 12:13])

linear = []
rfr = []
for i in range(0,len(prediction_data)):
    if i < len(prediction_data)/2:
        linear.append(prediction_data[i])
    else:
        rfr.append(prediction_data[i])

test_data = np.array(df.iloc[:, 15:26])



col = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]

for i in range(0, len(linear)):
    plt.plot(col, linear[i], label = 'Dane predykcyjne - model: regresja liniowa')
    plt.plot(col, rfr[i], label='Dane predykcyjne - model: las losowy')
    plt.plot(col, test_data[i], label = 'Dane rzeczywiste')
    plt.xlabel("Wartość w czasie - jedna godzina (przedział 5 minutowy)")
    plt.ylabel("Kurs BTC (USD)")
    plt.title("Wykres danych predykcyjnych vs dane rzeczywiste")
    plt.legend()
    plt.show()
