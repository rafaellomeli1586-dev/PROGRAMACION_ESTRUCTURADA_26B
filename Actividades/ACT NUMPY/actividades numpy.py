#-----------------EJERCICIO 1--------------#
import numpy as np

sistolica = np.array([118, 135, 142, 110, 128, 155, 121])

# a) Promedio y desviación estándar
promedio = np.mean(sistolica)
desv_estandar = np.std(sistolica)

print(f"Promedio: {promedio}")
print(f"Desviación estándar: {desv_estandar}")

# b) Cuántas lecturas son >= 130 mmHg usando una máscara booleana
mascara = sistolica >= 130
cantidad = np.sum(mascara)
print(f"Cantidad de lecturas >= 130: {cantidad}")

# c) Posiciones de esas lecturas
posiciones = np.flatnonzero(mascara)
print(f"Posiciones: {posiciones}")

#------------------EJERCICIO 2-----------------#
import numpy as np

glucosa = np.array([
    [ 95, 102,  89],
    [140, 155, 148],
    [ 88,  91,  85],
    [110, 118, 123]
])

# a) Promedio de glucosa por paciente (por filas -> axis=1)
promedio_pacientes = np.mean(glucosa, axis=1)
print("a) Promedio por paciente:", promedio_pacientes)

# b) Promedio por día (por columnas -> axis=0) y el día más alto
promedio_dias = np.mean(glucosa, axis=0)
dia_mas_alto = np.argmax(promedio_dias)
print("b) Promedio por día:", promedio_dias)
print(f"   El día con el promedio más alto fue el día: {dia_mas_alto + 1} (índice {dia_mas_alto})")

# c) Paciente y día que tuvieron el valor máximo absoluto
indice_plano = np.argmax(glucosa)
paciente, dia = np.unravel_index(indice_plano, glucosa.shape)
valor_maximo = glucosa[paciente, dia]

print(f"c) El valor máximo fue {valor_maximo} mg/dL")
print(f"   Corresponde al Paciente {paciente + 1} (fila {paciente}) en el Día {dia + 1} (columna {dia})")

#---------------EJERCICIO 3----------------#
import numpy as np

datos = np.array([
    [36.5,  72,  95],
    [38.2, 104, 140],
    [37.0,  80,  88],
    [36.8,  85, 110],
    [39.1, 112, 123]
])

# a y b) Normalización min-max por columnas sin usar ningún ciclo for
# axis=0 calcula el mínimo y máximo de cada columna (forma shape: (3,))
min_vals = datos.min(axis=0)
max_vals = datos.max(axis=0)

# Aplicamos la fórmula aprovechando el broadcasting de NumPy
datos_norm = (datos - min_vals) / (max_vals - min_vals)

print("a y b) Datos normalizados:")
print(datos_norm)

# c) Verificación de mínimos y máximos por columna
min_verif = datos_norm.min(axis=0)
max_verif = datos_norm.max(axis=0)

print("\nc) Verificación de mínimos por columna:", min_verif)
print("   Verificación de máximos por columna:", max_verif)