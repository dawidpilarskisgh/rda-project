import matplotlib.pyplot as plt
import pandas as pd


dictionary = [
    ['sentiment_text_blob', 'Likes', '0'],
    ['sentiment_text_blob', 'RTs', '0'],
    ['sentiment_text_blob', 'len', '0'],
    ['Positive_nltk', 'Likes', '0'],
    ['Negative_nltk', 'Likes', '0'],
    ['Positive_nltk', 'Negative_nltk', '0'],
    ['Positive_nltk', 'RTs', '0'],
    ['Negative_nltk', 'RTs', '0'],
    ['Positive_nltk', 'len', '0'],
    ['Negative_nltk', 'len', '0']

]

plot_df = pd.read_csv('data/data_to_prediction_model_v2.csv')

for i in dictionary:

    fig, ax = plt.subplots(figsize=(15,7))
    fig.subplots_adjust(right=0.75)

    l1,=ax.plot(plot_df[i[0]],'r')
    ax.set_ylabel(i[0])

    ax2=ax.twinx()
    l2,=ax2.plot(plot_df[i[1]],'g')
    ax2.set_ylabel(i[1])

    ax3=ax.twinx()
    l3,=ax3.plot(plot_df[i[2]],'b')
    ax3.set_ylabel(i[2])
    ax3.spines["right"].set_position(("axes", 1.2))
    ax3.spines["right"].set_visible(True)

    ax.legend((l1,l2,l3),(i[0], i[1] ,'BTC price'),loc='upper center', bbox_to_anchor=(0.5, 1.05),
          ncol=3, fancybox=True, shadow=True)

    plt.show()

