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

Program podzielony na mniejsz programy, które wykonują się w odpowiedniej koljeności, zgodnie z załączonym powyżej zdjęciem.

Program:
* twitter_data - odpowiada za ściągnięcie danych z twittera oraz analizę sentymentu,
* btc_data - ściąga dane z yfinance, cen bitcoina,
* data_preparation - przygptpwuje dane (agreguje, liczy średnią(
* create_model - trenuje wybrane model 
* prediction - przeprowadzenie predykcji,
* generate_raport - wygenerowanie wykresów na najbliższą godzinę. 


### Wyniki trenowania modelu na danych historycznych (ostatnie 7 dni):

![image](https://user-images.githubusercontent.com/91250294/150600027-6930b01a-73c4-4563-9e8a-2df268251a94.png)
