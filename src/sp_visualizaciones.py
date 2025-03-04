import matplotlib.pyplot as plt
import seaborn as sns

def graficar_histograma(df, columna, bins=30):
    """Genera un histograma para visualizar la distribución de una variable."""
    plt.figure(figsize=(8,5))
    sns.histplot(df[columna], bins=bins, kde=True)
    plt.title(f"Distribución de {columna}")
    plt.xlabel(columna)
    plt.ylabel("Frecuencia")
    plt.show()

def graficar_boxplot(df, columna):
    """Genera un boxplot para identificar outliers."""
    plt.figure(figsize=(8,5))
    sns.boxplot(x=df[columna])
    plt.title(f"Boxplot de {columna}")
    plt.xlabel(columna)
    plt.show()
