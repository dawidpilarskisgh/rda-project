import matplotlib.pyplot as plt
import numpy as np

def make_plot(data):
    df = data
    prediction_data = np.array(df.iloc[:, :11])

    linear_blob = []
    linear_nltk = []
    rfr_blob = []
    rfr_nltk = []

    linear_blob.append(prediction_data[0])
    rfr_blob.append(prediction_data[1])
    linear_nltk.append(prediction_data[2])
    rfr_nltk.append(prediction_data[3])

    col = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]

    plt.plot(col, linear_blob[0], label='Predykcja- model: RegL, sent:TB')
    plt.plot(col, rfr_blob[0], label='Predykcja- model: LasL, sent:TB')
    plt.plot(col, linear_nltk[0], label='Predykcja- model: RegL, sent: NLTK')
    plt.plot(col, rfr_nltk[0], label='Predykcja- model: LasL, sent:NLTK')
    plt.xlabel("Wartość w czasie - jedna godzina (przedział 5 minutowy)")
    plt.ylabel("Kurs BTC (USD)")
    plt.title("Wykres danych predykcyjnych")
    box = plt.subplot(111).get_position()
    plt.subplot(111).set_position([box.x0, box.y0, box.width * 0.8, box.height])
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()

