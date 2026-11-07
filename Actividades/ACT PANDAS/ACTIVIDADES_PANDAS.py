#------------EJERCICIO 4--------------#
import pandas as pd

df = pd.read_excel("pacientes.xlsx", sheet_name="pacientes")

#a)¿Cuantos pacientes y cuantas columnas hay?
print("--- a) Dimensiones ---")
print(f"Filas (pacientes) y Columnas: {df.shape}")
#b)¿Que columnas tienen faltantes y cuantos?
print("\n--- b) Valores Faltantes ---")
nulos = df.isnull().sum()
print(nulos[nulos>0])
#c)¿Que tipo de dato tiene cada columna?
print("\n--- c) Tipos de datos ---")
print(df.dtypes)

#-----------EJERCICIO 5----------#
filtro_alerta = (df['temp_c'] >= 38) & (df['fc_lpm'] > 100)
df_alerta = df[filtro_alerta]

# a) y b) ¿CUANTOS SON Y MOSTRAR ID, TEMP_C, FC_LPM Y SERVICIO?
print("\n--- EJERCICIO 5---")
print(f"Total de pacientes con fiebre y taquicardia: {len(df_alerta)}")
print("\nDatos solicitados (id, temp_c, fc_lpm, servicio):")
print(df_alerta[['id', 'temp_c', 'fc_lpm', 'servicio']])
# c) ¿En que servicio estan?
print("\nConteo por servicio:")
print(df_alerta['servicio'].value_counts())

#-----------EJERCICIO 6---------#

df['estatura_m'] = pd.to_numeric(df['estatura_m'], errors='coerce')
df['peso_kg'] = pd.to_numeric(df['peso_kg'], errors='coerce')

# a) Crea la columna imc = peso / estatura^2
df['imc'] = df['peso_kg'] / (df['estatura_m'] ** 2)

# b) Clasifícala: < 18.5 bajo peso, 18.5-24.9 normal, 25-29.9 sobrepeso, >= 30 obesidad
bins = [0, 18.5, 25, 30, 1001]
labels = ["Bajo peso", "Normal", "Sobrepeso", "Obesidad"]

# right=False hace que los intervalos sean cerrados a la izquierda: [18.5, 25)
df['categoria_imc'] = pd.cut(df['imc'], bins=bins, labels=labels, right=False)

# c) Cuenta pacientes por categoría y analiza los faltantes
print("\n--- EJERCICIO 6 ---")
print("Conteo de pacientes por categoría de IMC:")
print(df['categoria_imc'].value_counts(dropna=False))

print(f"\nCantidad de pacientes sin IMC: {df['imc'].isnull().sum()}")

#-----------EJERCICIO 7----------#

# --- EJERCICIO 7: Resumen por servicio ---

resumen = (
    df.groupby("servicio")
    .agg(
        num_pacientes=("id", "count"),
        temp_promedio=("temp_c", "mean"),
        fc_promedio=("fc_lpm", "mean")
    )
    .round(1)
    .sort_values(by="fc_promedio", ascending=False)
)

print("\n--- EJERCICIO 7: Resumen por servicio ---")
print(resumen)

