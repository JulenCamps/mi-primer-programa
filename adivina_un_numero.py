number_to_guess = int(input("Que numero tiene que adivinar tu contrincantne?:"))
number_guessed = int(input("Adivina el numero:"))


while number_to_guess != number_guessed:
    number_guessed = int(input("Adivina el numero:"))

if number_guessed == number_to_guess:
    print("Has ganado")





