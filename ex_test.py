import pandas as pd
from openpyxl import load_workbook


def crear_archivo_excel(datos, nombre_archivo):
    # Crear un DataFrame a partir del diccionario de datos
    df = pd.DataFrame(datos)

    # Guardar el DataFrame en un archivo Excel
    df.to_excel(nombre_archivo, index=False)


# Ejemplo de uso
datosIniciales = {
    'Codigo': ['601'],
    'Descripcion': ['Relleno vending'],
    'Cantidad': [19]
}

def InicializarExcel():
    crear_archivo_excel(datosIniciales,'produccion')

def nueva_fila_excel(ruta_archivo, valores):
    """
    Añade una fila de valores a un archivo Excel existente.

    :param ruta_archivo: Ruta del archivo Excel existente.
    :param valores: Lista de valores que se van a añadir como una nueva fila.
    """
    # Cargar el archivo Excel existente
    libro = load_workbook(ruta_archivo)
    
    # Seleccionar la hoja activa
    hoja = libro.active
    
    # Añadir la nueva fila
    hoja.append(valores)
    
    # Guardar los cambios
    libro.save(ruta_archivo)




