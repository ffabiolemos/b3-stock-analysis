import seaborn as sns
import matplotlib.pyplot as plt


def plotar_preco(precos):
    """
    Gera um gráfico de linha com a evolução do preço da ação
    ao longo do período analisado.
    """
    sns.lineplot(x=precos.index, y=precos.values)
    plt.title("Preço da Ação (12 meses)")
    plt.xlabel("Data")
    plt.ylabel("Preço (R$)")
    plt.show()


def plotar_dividendos(dividendos):
    """
    Plota o histórico de dividendos pagos pela ação.
    Caso não exista histórico, informa o usuário.
    """
    if dividendos.empty:
        print("A ação não possui histórico de dividendos.")
        return

    sns.lineplot(x=dividendos.index, y=dividendos.values)
    plt.title("Histórico de Dividendos")
    plt.xlabel("Data")
    plt.ylabel("Valor")
    plt.show()
