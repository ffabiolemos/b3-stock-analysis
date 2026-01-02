from src.fetch_data import (
    carregar_acao,
    obter_info_basica,
    obter_dividendos,
    obter_preco_historico
)
from src.indicators import (
    calcular_retorno,
    calcular_volatilidade
)
from src.visualization import (
    plotar_preco,
    plotar_dividendos
)
from src.report import gerar_relatorio


def main():
    ticker = input("Digite o ticker da ação (ex: PETR4.SA): ")

    acao = carregar_acao(ticker)

    info = obter_info_basica(acao)
    dividendos = obter_dividendos(acao)
    precos = obter_preco_historico(acao)

    retorno = calcular_retorno(precos)
    volatilidade = calcular_volatilidade(precos)

    gerar_relatorio(info, retorno, volatilidade)
    plotar_preco(precos)
    plotar_dividendos(dividendos)


if __name__ == "__main__":
    main()
