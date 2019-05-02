que_quiere = input("Tienes que calcular un cateto o una hiputenusa? (Cateto/Hipotenusa):").upper()
import math

if que_quiere == "CATETO":
    hipotenusa = int(input("Dime el valor de la hipotenusa:"))
    cateto = int(input("Dime el valor del cateto:"))
    hipotenusa_2 = hipotenusa ** 2
    cateto_2 = cateto ** 2
    total = hipotenusa_2 - cateto_2
    numero_final = math.sqrt(total)
    print("El cateto mide: {}".format(numero_final))

elif que_quiere == "HIPOTENUSA":
    cateto_g = int(input("Dime el valor del cateto mas grande:"))
    cateto_p = int(input("Dime el valor del cateto pequeño:"))
    cateto_g_2 = cateto_g ** 2
    cateto_p_2 = cateto_p ** 2
    total = cateto_g_2 + cateto_p_2
    numero_final = math.sqrt(total)
    print("La hipotenusa mide: {}".format(numero_final))

