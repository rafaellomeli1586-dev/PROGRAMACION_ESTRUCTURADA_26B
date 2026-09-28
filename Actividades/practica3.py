pin_correcto = int(input("PIN CORRECTO: "))

intentos = 0
aciertos = False

while intentos < 3 and aciertos == False:
    pin = int(input("PIN: "))
    intentos = intentos + 1

    if pin == pin_correcto:
        aciertos = True

if aciertos == True:
    print("ACCESO")
else:
    print("DENEGADO")
