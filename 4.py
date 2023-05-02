## Adivina el numero de la computadora con 3 vidas

import random


print("===============================")
print("Bienvenido a Adivina el numero")
print("Tu meta es adivinar el numero generado por la computadora")
print("===============================")
x = int(input("Ingrese un numero de limite: "))


def adivina_el_numero(x):
    numAle = random.randint(1,x)

    preddition = 0
    vida = 3

    while preddition != numAle:
        preddition = int(input(f"Ingrese un numero entre 1 y {x}: "))

        if preddition < numAle:
            print("El numero es mayor")
            if vida != 0:
                vida -= 1
                print(f"Te quedan {vida} vidas")
        elif preddition > numAle:
            print("El numero es menor")
            if vida != 0:
                vida -= 1
                print(f"Te quedan {vida} vidas")
        if vida == 0:
            print("Perdiste")
            break
    if preddition == numAle:
        print(f"Felicidades, has adivinado el numero {numAle} correctamente")


adivina_el_numero(x)