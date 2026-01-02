import pandas as pd


def calcular_retorno(precos: pd.Series):
    """
    Calcula o retorno percentual do período analisado,
    considerando o primeiro e o último preço da série.
    """
    return (precos.iloc[-1] / precos.iloc[0]) - 1


def calcular_media_movel(precos: pd.Series, janela=20):
    """
    Calcula a média móvel simples (SMA),
    muito utilizada para identificar tendências de preço.
    """
    return precos.rolling(window=janela).mean()


def calcular_volatilidade(precos: pd.Series):
    """
    Calcula a volatilidade com base no desvio padrão
    dos retornos diários da ação.
    """
    retornos_diarios = precos.pct_change()
    return retornos_diarios.std()
