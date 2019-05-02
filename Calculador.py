operacion = input("¿Que operacion quieres hacer? (Suma / Resta / Multiplicacion / Division:").upper()
numero_1 = int(input("Prmer Numero:"))
numero_2 = int(input("Segundo numero:"))

if operacion == "SUMA":
    resultado = numero_1 + numero_2

elif operacion == "RESTA":
    resultado = numero_1 - numero_2

elif operacion== "MULTIPLICACION":
    resultado = numero_1 * numero_2

elif operacion== "DIVISION":
    resultado = numero_1 / numero_2

print("El resultado de tu operacion es: {}".format(resultado))


