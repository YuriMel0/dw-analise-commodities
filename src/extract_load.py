import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os 

commodities = ['CL=F', 'GC=F', 'SI=F']

def buscar_dados_commodities(simbolo, periodo='5y', intervalos='1d'):
    ticker = yf.Ticker('CL=F')
    dados = ticker.history(period=periodo, interval=intervalos)[['Close']]
    dados['simbolo'] = simbolo
    return dados

def agrupar_dados_commodities(comodities):
    todos_dados = []
    for simbolo in commodities:
        dados = buscar_dados_commodities(simbolo)
        todos_dados.append(dados)
    return pd.concat(todos_dados)