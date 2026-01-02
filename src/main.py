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
    # Entrada do usuário: ticker da ação no padrão do Yahoo Finance
    ticker = input("Digite o ticker da ação (ex: PETR4.SA): ")

    # Carrega o objeto da ação via API
    acao = carregar_acao(ticker)

    # Coleta dos dados necessários para análise
    info = obter_info_basica(acao)
    dividendos = obter_dividendos(acao)
    precos = obter_preco_historico(acao)

    # Cálculo dos principais indicadores financeiros
    retorno = calcular_retorno(precos)
    volatilidade = calcular_volatilidade(precos)

    # Geração do relatório textual
    gerar_relatorio(info, retorno, volatilidade)

    # Visualizações gráficas
    plotar_preco(precos)
    plotar_dividendos(dividendos)


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
