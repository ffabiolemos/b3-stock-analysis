def gerar_relatorio(info, retorno, volatilidade):
    """
    Exibe no terminal um resumo com as principais informações
    e indicadores da ação analisada.
    """
    print("\n📊 RELATÓRIO DA AÇÃO\n")
    print(f"Ação: {info['nome']}")
    print(f"Setor: {info['setor']}")
    print(f"Preço atual: R$ {info['preco_atual']}")
    print(f"Dividend Yield: {info['dividend_yield']}")
    print(f"Retorno no período: {retorno:.2%}")
    print(f"Volatilidade: {volatilidade:.4f}")
