import pandas as pd
import re

def limpiar_nombres_columnas(df):
    """
    Limpia los nombres de las columnas en un DataFrame:
    - Elimina espacios en blanco antes y después del nombre.
    - Convierte nombres en Title_Case con guiones bajos (_).
    - Reemplaza caracteres especiales por guiones bajos (_).
    - Inserta guiones bajos entre palabras si están en PascalCase o camelCase.

    Parámetros:
    - df: DataFrame de pandas.

    Retorna:
    - DataFrame con nombres de columnas limpios y en formato Title_Case.
    """
    df = df.copy()  # Para evitar modificar el original
    
    df.columns = (df.columns.str.strip()
                            .str.replace(r"([a-z])([A-Z])", r"\1_\2", regex=True)  # Separa PascalCase/camelCase
                            .str.replace(r"[^a-zA-Z0-9]", "_", regex=True)  # Reemplaza caracteres especiales
                            .str.replace(r"_+", "_", regex=True)  # Evita múltiples guiones bajos
                            .str.strip("_")
                            .str.lower()
                            .str.title()  # Convierte a formato Title_Case
                            )

    return df


def valores_unicos(df):
    """
    Muestra los valores únicos de cada columna en un DataFrame.

    Parámetros:
    df : pandas.DataFrame
        DataFrame del cual queremos analizar los valores únicos.

    Retorna:
    None (Imprime los valores únicos de cada columna en la consola)
    """
    for col in df.columns:
        print(f"🔹 Valores únicos en '{col}':")
        print(df[col].unique(), "\n")


def concatenar_nombres(df):
    """
    Concatena las columnas 'First_Name' y 'Last_Name' en una nueva columna 'Full_Name'.
    La nueva columna se coloca en la posición [1], después de 'Customer_Id'.
    Luego, elimina las columnas originales 'First_Name' y 'Last_Name'.

    Parámetros:
    df : pandas.DataFrame
        DataFrame que contiene las columnas 'First_Name' y 'Last_Name'.

    Retorna:
    df : pandas.DataFrame
        DataFrame con la nueva columna 'Full_Name' y sin 'First_Name' ni 'Last_Name'.
    """

    df = df.copy()  # Evita modificar el DataFrame original
    
    # Crear la nueva columna 'Full_Name'
    df["Full_Name"] = df["First_Name"].str.strip() + " " + df["Last_Name"].str.strip()

    # Mover 'Full_Name' a la posición [1] después de 'Customer_Id'
    cols = list(df.columns)
    cols.insert(1, cols.pop(cols.index("Full_Name")))  # Mueve 'Full_Name' a la posición 1
    df = df[cols]

    # Eliminar las columnas originales
    df.drop(columns=["First_Name", "Last_Name"], inplace=True)

    return df


