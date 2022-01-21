import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

#Tworzenie wykresu dla prognozy ceny Bitcoina

df = pd.read_csv('prediction_data.csv')

df = df.rename(columns={'0': '5', '1': '10','2': '15','3': '20','4': '25','5': '30','6': '35', '7': '40','8': '45','9': '50','10': '55', '0.1': '5', '1.1': '10','2.1': '15','3.1': '20','4.1': '25','5.1': '30','6.1': '35', '7.1': '40','8.1': '45','9.1': '50','10.1': '55'})
df=df.iloc[1:28,1:12 ]


fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(20, 8))

for row, ax in zip(df.index, axes.flatten()):
    ax.plot(df.loc[row].values)
    ax.set_title(row, fontsize=10)
    ax.set_xticks(range(df.shape[1]))
    ax.set_xticklabels(list(df.columns), rotation=90, fontsize=8)
plt.savefig('prediction_price.png')

#Tworzenie wykresu dla cen rzeczywistych Bitcoina

df = pd.read_csv('prediction_data.csv')

df = df.rename(columns={'0': '5', '1': '10','2': '15','3': '20','4': '25','5': '30','6': '35', '7': '40','8': '45','9': '50','10': '55', '0.1': '5', '1.1': '10','2.1': '15','3.1': '20','4.1': '25','5.1': '30','6.1': '35', '7.1': '40','8.1': '45','9.1': '50','10.1': '55'})
df=df.iloc[1:28,15:26 ]

fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(20, 8))

for row, ax in zip(df.index, axes.flatten()):
    ax.plot(df.loc[row].values)
    ax.set_title(row, fontsize=10)
    ax.set_xticks(range(df.shape[1]))
    ax.set_xticklabels(list(df.columns), rotation=90, fontsize=8)
plt.savefig('real_price.png')
