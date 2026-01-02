import pandas as pd


def calcular_retorno(precos: pd.Series):
    return (precos.iloc[-1] / precos.iloc[0]) - 1


def calcular_media_movel(precos: pd.Series, janela=20):
    return precos.rolling(window=janela).mean()


def calcular_volatilidade(precos: pd.Series):
    retornos_diarios = precos.pct_change()
    return retornos_diarios.std()
