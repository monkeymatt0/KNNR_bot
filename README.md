# Configurazione dell'ambiente virtuale
L'ambiente virtuale che viene utilizzato è un misto tra anaconda e pip. I pacchetti principali da installare sono:

- ccxt

- numpy

- pandas
- matplotlib
- seaborn
- plotly
- scikit-learn

Il mio IDE è Visual Studio Code. Con l'estensione per Jupyter Notebook.

Per effettuare l'installazione in maniera più veloce creare un file "requirements.txt" con tutte le librerire al suo interno.Una volta scritta una libreria bisogna andare a capo.
ES.
ccxt
numpy
pandas
.
.
.
.

Creare un ambiente virtuale.

Una volta creato l'ambiente virtuale, attivarlo, effettuare gli opportuni aggiornamenti(se ci sono) e poi usare il comando:
- pip install -r requirements.txt


# KNNR_bot

Questo bot (in fase primordiale) analizza come si comporta un modello KNNR per effettuare previsioni di mercato.
Ciò che proverò ad implementare è quello di andare a prevedere un intera candela e vedere come performa in relazione a tale previsione.
Le fasi saranno quelle classiche di un progetto di Data Science.

## Definizione

Nella parte di definizione si andrà a descrivere il problema e la solizione che si vuole implementare.
Ci sarà una prima parte in cui i dati non sono elaborati più di tanto, ovvero andremo a ragionare su un classico dataset OHLCV e successivamente si vedrà se aggiungere altri parametri come: ema, BB_bands, RSI ecc...
Ovviamente ogni nuova feature che vado ad aggiungere deve apportare un beneficio al modello altrimenti creo solo incremento di complessità senza benefici.

## Considerazioni

In futuro questo algoritmo potrebbe essere utilizzato in sincrono con altri modelli di ML per garantire una prestazione totale migliore.

In sostanza con KNNR andrò a valutare solo le CHIUSURE e massimo le APERTURE.

Per prevedere un intera candela andrò ad integrare il tutto con modelli che magari hanno una bias ridotto ed una varianza più elevata come ad esempio: DECISION-TREE-REGRESSOR o RANDOM-FOREST-REGRESSOR che data la loro natura dovrebbero essere più adatti a prevedere cose come i massimi e i minimi di una candela.
