import pandas as pd

df = pd.read_csv("Características y composición del hogar.csv", sep= ";")

print(df.head())
def limpieza_datos(df):
    """El objetivo de esta función es el de limpiar los datos
    del dataframe, debido a que nuestro trabajo se restringe principalmente a 
    personas de 18 años o mas, y que hayan vivido en bogotá los últimos 12 meses.

    Args:
        df (Dataframe) -> El archivo csv original
    Return 
        df (Dataframe) -> El Dataframe ya limpio con las variables a trabajar.
    """

    # 3. Filtrar por personas de 18 años o más, la variable p6040 se refiere a los años cumplidos de cada individuo
    df_mayores18 = df[df["P6040"] >= 18]

    # 4. Filtrar por personas que vivieron en Bogotá en los últimos 12 meses
    # La variable P753S1 indica en que departamento vivio en los ultimos 12 meses, el codigo 11 del "divipola" indica a bogota
    df_bogota = df_mayores18[df_mayores18["P753S1"] == 11]

    return df_bogota
# 5. Mostrar cuántos registros había antes y después del filtro
print("Total registros originales:", len(df))
print("Registros de personas mayores de 18 que vivieron en Bogotá:", len(limpieza_datos(df)))
