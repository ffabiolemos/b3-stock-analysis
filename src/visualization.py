import seaborn as sns
import matplotlib.pyplot as plt


def plotar_preco(precos):
    sns.lineplot(x=precos.index, y=precos.values)
    plt.title("Preço da Ação (12 meses)")
    plt.xlabel("Data")
    plt.ylabel("Preço (R$)")
    plt.show()


def plotar_dividendos(dividendos):
    if dividendos.empty:
        print("A ação não possui histórico de dividendos.")
        return

    sns.lineplot(x=dividendos.index, y=dividendos.values)
    plt.title("Histórico de Dividendos")
    plt.xlabel("Data")
    plt.ylabel("Valor")
    plt.show()
