import csv

def leer_y_procesar_csv(nombre_archivo):

    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)

        # Obtenemos los encabezados (la primera fila con los títulos)
        columnas = next(lector)

        # Obtenemos todas las filas de los pacientes en una lista
        filas = list(lector)

    return columnas, filas

# Bloque principal de ejecución
if __name__ == "__main__":
    # Nombres exactos de tus archivos en la carpeta
    archivo_mini = 'pacientes_mini - pacientes_mini.csv'
    archivo_extensa = 'pacientes - pacientes.csv'

    # 1. Leemos ambos archivos usando nuestra función
    cols_mini, filas_mini = leer_y_procesar_csv(archivo_mini)
    cols_extensa, filas_extensa = leer_y_procesar_csv(archivo_extensa)

    # 2. Juntamos las filas de ambas listas en una sola
    todas_las_filas = filas_extensa + filas_mini

    # 3. Buscamos en qué columna está el "nombre" para poder ordenar en base a él
    columnas_lower = [c.lower() for c in cols_extensa]

    if "nombre" in columnas_lower:
        indice_nombre = columnas_lower.index("nombre")
        todas_las_filas.sort(key=lambda x: x[indice_nombre])
    else:
        todas_las_filas.sort()

    # 4. Guardamos el resultado en un nuevo archivo CSV ordenado y unido
    archivo_salida = 'pacientes_unidos_y_ordenados.csv'
    with open(archivo_salida, mode='w', newline='', encoding='utf-8') as salida:
        escritor = csv.writer(salida)

        # Escribimos los encabezados primero
        escritor.writerow(cols_extensa)

        # Escribimos todas las filas ya ordenadas
        escritor.writerows(todas_las_filas)

    print("Proceso finalizado. El archivo se ha combinado y ordenado correctamente")
