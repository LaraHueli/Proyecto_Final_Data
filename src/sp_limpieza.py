import pandas as pd
import re
#------------------------------------------------------------------------------------------------------------------#
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
#------------------------------------------------------------------------------------------------------------------#
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
#------------------------------------------------------------------------------------------------------------------#
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
#------------------------------------------------------------------------------------------------------------------#
def limpiar_fechas(df, columnas_fecha):
    """
    Convierte las columnas de fecha a formato datetime y elimina la hora, dejando solo 'YYYY-MM-DD'.

    Parámetros:
    - df (pd.DataFrame): DataFrame con las columnas de fecha.
    - columnas_fecha (list): Lista con los nombres de las columnas a convertir.

    Retorna:
    - pd.DataFrame: DataFrame con las fechas en formato 'YYYY-MM-DD'.
    """
    df = df.copy()  # Para no modificar el original

    for col in columnas_fecha:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce').dt.date  # Convierte y deja solo la fecha

    return df
#------------------------------------------------------------------------------------------------------------------#
def calcular_edad(df, columna_fecha_nacimiento, columna_resultado="Edad"):
    df = df.copy()

    if columna_fecha_nacimiento in df.columns:
        df[columna_fecha_nacimiento] = pd.to_datetime(df[columna_fecha_nacimiento], errors='coerce').dt.date  # Eliminar la hora
        hoy = pd.to_datetime("today").date()
        df[columna_resultado] = df[columna_fecha_nacimiento].apply(lambda x: hoy.year - x.year if pd.notnull(x) else None)

        # Reordenar la columna de edad después de la fecha de nacimiento
        columnas = list(df.columns)
        idx = columnas.index(columna_fecha_nacimiento)
        columnas.insert(idx + 1, columnas.pop(columnas.index(columna_resultado)))
        df = df[columnas]

    return df
#------------------------------------------------------------------------------------------------------------------#
def años_trabajados(df, columna_fecha_ingreso, columna_resultado="Años_Trabajados"):
    df = df.copy()

    if columna_fecha_ingreso in df.columns:
        df[columna_fecha_ingreso] = pd.to_datetime(df[columna_fecha_ingreso], errors='coerce').dt.date  # Eliminar la hora
        hoy = pd.to_datetime("today").date()
        df[columna_resultado] = df[columna_fecha_ingreso].apply(lambda x: hoy.year - x.year if pd.notnull(x) else None)

        # Reordenar la columna de años trabajados después de la fecha de contratación
        columnas = list(df.columns)
        idx = columnas.index(columna_fecha_ingreso)
        columnas.insert(idx + 1, columnas.pop(columnas.index(columna_resultado)))
        df = df[columnas]

    return df
#------------------------------------------------------------------------------------------------------------------#
def convertir_a_entero(df, columnas):
    df = df.copy()
    for col in columnas:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)  # Convertir a entero
            print(f"✅ Columna {col} convertida a entero")  # Mensaje de confirmación
    return df
#------------------------------------------------------------------------------------------------------------------#
def separar_fecha_hora(df, columna_fecha):
    """
    Separa una columna de fecha en tres nuevas columnas:
    - 'Day_Sales' con la fecha (YYYY-MM-DD).
    - 'Hour_Full' con la hora completa (HH:MM:SS).
    - 'Hour_Sales' con solo la hora en formato numérico (0-23).

    Parámetros:
    - df (DataFrame): DataFrame de pandas con la columna de fecha.
    - columna_fecha (str): Nombre de la columna que contiene la fecha con hora.

    Retorna:
    - DataFrame con tres nuevas columnas.
    """
    df[columna_fecha] = pd.to_datetime(df[columna_fecha], errors="coerce")

    # Crear nuevas columnas
    df["Day_Sales"] = df[columna_fecha].dt.date  # Solo fecha
    df["Hour_Full"] = df[columna_fecha].dt.time  # Hora completa HH:MM:SS
    df["Hour_Sales"] = df[columna_fecha].dt.hour  # Solo la hora numérica (int)

    return df



