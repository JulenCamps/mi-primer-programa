rival = input("Contra que pokemon quieres convatir? (Squirtle / Charmander / Bulbasur:").upper()
vida_pikachu = 100
vida_enemigo = 0
if rival == "SQUIRTLE":
    vida_enemigo = 90
    nombre_enemigo = "Sqirtle"
    ataque_enemigo = 10
elif rival == "CHARMANDER":
    vida_enemigo = 80
    nombre_enemigo = "Charmander"
    ataque_enemigo = 7
elif rival == "BULBASUR":
    vida_enemigo = 100
    nombre_enemigo = "Bulbasur"
    ataque_enemigo = 11


while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_seleccionado = input("Elije un ataque (Fuego infernal / Ascuas):").upper()
    if ataque_seleccionado == "FUEGO INFERNAL":
        vida_enemigo = vida_enemigo - 10
    if ataque_seleccionado == "ASCUAS":
        vida_enemigo = vida_enemigo -12
        print("Vida enemigo:{}".format(vida_enemigo))

   print("{} te ha quitado {} puntos de vida".format(nombre_enemigo, ataque_enemigo))
    vida_pikachu -= ataque_enemigo

if vida_pikachu <0:
    print("Has perdido")
else:
    print("Has ganado")


