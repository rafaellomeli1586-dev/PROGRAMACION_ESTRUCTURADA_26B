#ENTRADAS DE DATOS.

saldo = float(input("Ingresa el saldo disponible: "))
retirado = float(input("Ingresa el monto retirado hoy: "))
monto = int(input("Ingresa el monto a retirar: "))

#COMPROBACION 1: El monto debe ser multiplo de 50
if monto %50 != 0:
    mensaje = "MONTO NO VALIDO"

#COMPROBACION 2: El monto no puede ser mayor que el saldo
elif monto > saldo:
    mensaje = "SALDO INSUFICIENTE"

#COMPROBACION 3: Lo retirado hoy más el monto no puede pasar de 6000
elif (retirado + monto) > 6000:
    mensaje = "LÍMITE DIARIO EXCEDIDO"

# Si pasa las tres comprobaciones
else:
    saldo = saldo - monto
    mensaje = "ENTREGADO"

#Salida con el formato especificado: <MENSAJE> | saldo: <saldo>
if saldo.is_integer():
    saldo = int(saldo)
print(f"{mensaje} | saldo: {saldo}")
