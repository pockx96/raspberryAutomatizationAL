import pandas as pd


def crear_archivo_excel(datos, nombre_archivo):
    # Crear un DataFrame a partir del diccionario de datos
    df = pd.DataFrame(datos)

    # Guardar el DataFrame en un archivo Excel
    df.to_excel(nombre_archivo, index=False)

# Ejemplo de uso
datos = {
    'Codigo': ['601'],
    'Descripcion': ['Relleno vending'],
    'Cantidad': [19]
}

nombre_archivo = 'vending.xlsx'
crear_archivo_excel(datos, nombre_archivo)

