#PRACTICA1 DIAGRAMA DE FLUJO1

temp = float(input("Ingrese la temperatura: "))
fc = int(input("Ingrese la frecuencia: "))
sat = int(input("Ingrese la saturacion de oxigeno: "))

if sat < 90 or fc > 120:
    print("ROJO")
elif temp >= 39:
    print("AMARILLO")
else:
    print("VERDE")
