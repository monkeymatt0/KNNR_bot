'''
In questa parte vado a creare tutte le componenti che mi consentono di gestire i dati e di elaborarli in maniera opportuna
'''

import ccxt
from pprint import pprint as pp
import pandas as pd
import numpy as np
from datetime import datetime
import os


'''
Funzione per recuperare i dati.
I dati vengono salvati in csv all'interno del file: data/nome_file.csv
I nome che verrano dati ai file sono nomi standardizzati e avranno questo formato:
{coppia_trading}_OHLCV_daily.csv

Ritorna il path del file
'''
def date_adjuster(df: pd.DataFrame) -> pd.DataFrame:
     df["date"] = 0
     for index, record in df.iterrows():
          df.at[index, "date"] = datetime.fromtimestamp((record["timestamp"]/1000))
     df.drop(columns=["timestamp"], inplace=True)
     return df

def retriever(symbol: str, since: str) -> pd.DataFrame:
     binance = ccxt.binance()
     json_OHLCV = binance.fetch_ohlcv(symbol=symbol, timeframe="1d", limit=1000, since=binance.parse8601(since))
     df = pd.DataFrame(data=json_OHLCV, columns=["timestamp", "O", "H", "L", "C", "V"])
     return df


def data_retriever_daily(symbol: str) -> str:
     binance = ccxt.binance()

     if binance.has['fetchOHLCV']:
          print(20*"*", "OK")
          json_OHLCV = None
          df = None
          df2 = None
          ret = "data"
          filename = f"{symbol.split('/')[0]}-{symbol.split('/')[1]}_OHLCV_daily.csv"
          try:
               df = retriever(symbol=symbol, since="2019-09-19 02:00:00")
               df = date_adjuster(df)
               df2 = retriever(symbol=symbol, since=str(df.index[len(df) - 1]))
               df2 = date_adjuster(df2)
               df = pd.concat([df, df2], ignore_index=True)
          except Exception as ex:
               pass
          finally:
               # Scrittura del file
               df.to_csv(os.path.join(ret, filename))
     else:
          print(20*"#", "OHLCV fetching not possible....")

     return os.path.join(ret, filename)