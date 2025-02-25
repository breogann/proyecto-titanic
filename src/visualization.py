import seaborn as sns
import matplotlib.pyplot as plt

def histograma_edad (df):
    sns.histplot(df["age"], bins=30)
    plt.title("DISTRIBUCIÓOOOOOON EDAD") # se cierra el plt;
    plt.savefig("images/histograma_edad.png");

def survival_plot (df):
    sns.countplot(x="sex", hue="survived", data=df)
    plt.savefig("images/survival_plot.png");