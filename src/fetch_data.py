import yfinance as yf


def carregar_acao(ticker: str):
    """
    Retorna o objeto da ação a partir do ticker.
    Ex: 'PETR4.SA'
    """
    return yf.Ticker(ticker)


def obter_info_basica(acao):
    info = acao.info

    # Retorna apenas os dados mais relevantes para análise inicial
    return {
        "nome": info.get("shortName"),
        "setor": info.get("sector"),
        "preco_atual": info.get("currentPrice"),
        "dividend_yield": info.get("dividendYield"),
        "market_cap": info.get("marketCap"),
    }


def obter_dividendos(acao):
    # Retorna o histórico de dividendos pagos pela ação
    # (pode ser uma Series vazia se a empresa não pagar dividendos)
    return acao.dividends


def obter_preco_historico(acao, periodo="1y"):
    # Obtém o histórico de preços no período definido
    # Utilizado apenas o preço de fechamento ("Close")
    return acao.history(period=periodo)["Close"]
