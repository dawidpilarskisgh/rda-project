# Projekt zaliczeniowy na przedmiot Analiza danych w czasie rzeczywistym
#### Semestr zimowy 2021/2022, SGH Szkoła Główna Handlowa w Warszawie

#### Wykonali:
* Miętus Karolina
* Pilarski Dawid 
* Gorczyca Kamil
* Gliczyński Maciej
* Szwalikowski Rafał

## Tytuł projektu: *Analiza danych - ceny kryptowalut w czasie rzeczywistym na podstawie danych z Twittera*

### Wstęp: 
Projekt polega na pobieraniu danych z portalu społecznościowego Twitter, po czym posty są analizowane pod kątem sentymentu. Pobierane są rónwnież dane, takie jak: długość wpisu, liczba polubień, liczba retweetów.

Analiza odbywa się w czasie rzeczywistym, przy założeniach:
* szukane słowa w tweetach dotyczące bitocoina: WORDS_TO_SEARCH = ['bitcoin', 'crypto', 'cryptonews', 'cryptocurrency', 'cryptocurrencies', 'BTC', 'bitmark', 'binance', 'bitbay', 'blockchain', 'PaidInBitcoin'],
* dane z Twittera gromadzone są z ostatniej godziny, 
* dane są analizowane, po czym wyciągana jest średnia wartość,
* predykcja cen bitcoin'a jest obrazowana na następną godzinę w odstępie 5 minutowym (ceny na jedną godzinę, co 5 minut), 
* model predykcyjny gormadzi raz dziennie dane po czym "doucza się".

Wykorzystywane API w projekcie: 
* tweepy - do pobierania danych z Twittera,
* yfinance - do pobierania cen bitocoin'a.

Ograniczenia w projekcie spowodowane API tweepy:
* dane do nauki zostały pobrane wyłącznie z ostatnich 7 dni, okres nie może zostać wydłużony,
* jeden request do API zwraca tylko 100 losowych wyników

Wykorzystane model predykcyjne: 
* regresja linijowa,
* las losowy.

Sentyment jest analizowany na dwa sposoby z wykorzystaniem  bibliotek:
* nltk.sentiment.vader --> SentimentIntensityAnalyzer,
* textblob.

### Opis programu: 
![image](https://user-images.githubusercontent.com/91250294/150602503-0a14985c-dea3-480e-b5c7-c3cf36c0dc6b.png)

Program podzielony na mniejsze programy, które wykonują się w odpowiedniej koljeności, zgodnie z załączonym powyżej zdjęciem.

Program:
* twitter_data - odpowiada za ściągnięcie danych z twittera oraz analizę sentymentu,
* btc_data - ściąga dane z yfinance, cen bitcoina,
* data_preparation - przygptpwuje dane (agreguje, liczy średnią(
* create_model - trenuje wybrane model 
* prediction - przeprowadzenie predykcji,
* generate_raport - wygenerowanie wykresów na najbliższą godzinę. 


### Wyniki trenowania modelu na danych historycznych (ostatnie 7 dni):
Pobrany zbiór został podzielony na testowy oraz treninowy. 
Wytrenowane modele ( [textblob, linijowa regresja], [textblob, las losowy], [NLTK, linijowa regresja], [NLTK, las losowy], zostały poddane ocenie na zbiorze testowy.
Poniżej otrzymane wyniki: 

###### Analiza sentymentu wykonana sposobem: TextBlob.
###### Predykcja wykonana modelem: Linear_Regression.
###### Oceny modelu: 
* R2 score: 0.9794486803153529
* MAE: 66.08374832422122
* MSE: 6839.784588030288
* RMSE : 82.70299020005436

###### Analiza sentymentu wykonana sposobem: TextBlob.
###### Predykcja wykonana modelem: RandomForest.
###### Oceny modelu: 
* R2 score: 0.9648706670396993
* MAE: 86.00596387987015
* MSE: 11558.784041519437
* RMSE : 107.51178559357777

###### Analiza sentymentu wykonana sposobem: NLTK.
###### Predykcja wykonana modelem: Linear_Regression.
###### Oceny modelu: 
* R2 score: 0.97674086707298
* MAE: 71.00403009967353
* MSE: 7811.261562111479
* RMSE : 88.38134170802952

###### Analiza sentymentu wykonana sposobem: NLTK.
###### Predykcja wykonana modelem: RandomForest.
###### Oceny modelu: 
* R2 score: 0.9648390539371866
* MAE: 86.03887860186677
* MSE: 11544.754741718189
* RMSE : 107.44652037976003

###### Poniżej wykresy pokazujące ceny dla danych predykcyjnych vs rzeczywiste:
- model: Regl = Model regresji liniowej,
- model: LasL = Model Las losowy,
- sent: TB = sentyment określony przy pomocy TextBlob,
- sent: NLTK = sentyment określony przy pomocy NLTK

###### 1  
![image](https://user-images.githubusercontent.com/91250294/150606477-c95bd954-f4e9-4a25-98ca-cd0a3a9bd3f5.png)

###### 2
![image](https://user-images.githubusercontent.com/91250294/150606584-3b784d59-9abb-493a-aca0-fe19127872d1.png)

###### 3 
![image](https://user-images.githubusercontent.com/91250294/150606606-c2bcf72b-7088-4f2a-af73-cb738c117ab0.png)

###### 4 
![image](https://user-images.githubusercontent.com/91250294/150606644-aab00a9d-65de-4123-a61a-7fca4d3d17f2.png)

###### 5
![image](https://user-images.githubusercontent.com/91250294/150606678-0ac8e67a-2eac-43e1-ba63-ba373ca026c7.png)

###### 6
![image](https://user-images.githubusercontent.com/91250294/150606707-2cfa0968-8c0b-4702-840c-4e9719a4346a.png)

###### 7
![image](https://user-images.githubusercontent.com/91250294/150606734-d40db16a-8440-46e5-863c-b4101f033ad8.png)


### Eksploracja zbioru
Porównanie zależności między zminnymi objaśniającymi (długość tweeta, liczba retweetów, liczba lików, sentyment) a ceną bitcoina.

![image](https://user-images.githubusercontent.com/91250294/150614647-61b6ed1f-09f6-45a1-b12d-34d57fa7213c.png)


![image](https://user-images.githubusercontent.com/91250294/150614668-5ff4d792-2730-4f55-a8af-22055fbf3f10.png)


![image](https://user-images.githubusercontent.com/91250294/150614681-4ee6d28c-3533-4d9c-b4c1-7c1c7533d6cc.png)


![image](https://user-images.githubusercontent.com/91250294/150614697-c075e01d-ed08-44e6-ac9a-91d6ee359168.png)


![image](https://user-images.githubusercontent.com/91250294/150614710-567add40-d8fd-4fb0-bf96-cc09769d4d13.png)


![image](https://user-images.githubusercontent.com/91250294/150614726-cc0ba1c8-be5b-4681-9125-9e4c60bd2fc1.png)


![image](https://user-images.githubusercontent.com/91250294/150614736-f7f69165-4ea4-415d-9890-cef986205c2e.png)


![image](https://user-images.githubusercontent.com/91250294/150614748-7bae1083-b0ce-4b16-8293-ec063d1f2cbc.png)


![image](https://user-images.githubusercontent.com/91250294/150614761-a407ce03-c8e6-4f10-acba-ff6505127a02.png)


![image](https://user-images.githubusercontent.com/91250294/150614773-773a2da2-58ad-461c-9b5b-e696909e7c69.png)

### Podsumowanie
Program dokonuje analizy sentymentów użytkowników Twittera i na ich podstawie tworzy predykcję cen Bitcoina. Ze względu na krótkookresową prognozę cen program jest słabym narzędziem wspierającym długookresowe inwestycja, ale może mieć np. zastosowanie w przypadku dokonywania transakcji spekulacyjnych przez day-traderów. Na podstawie analizy danych historycznych w porównaniu do prognoz cen dokonanych przez wykorzystane modele lepszą mocą predykcyjną charakteryzował się model wykorzystujący regresję liniową zwłaszcza na podstawie analizy sentymentu wykonanej sposobem TextBlob.




