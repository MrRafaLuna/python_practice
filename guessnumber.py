import random

numero_a_adivinar = random.randint(1, 50)
numero_ingresado = None

while numero_ingresado != numero_a_adivinar:
    numero_ingresado = int(input("Adivina un número entre 1 y 50: "))
    if numero_ingresado < 1 or numero_ingresado > 50:
        print("El número debe estar entre 1 y 50. Intenta de nuevo.")
    elif numero_ingresado < numero_a_adivinar:
        print("Intenta con un número más grande.")
    elif numero_ingresado > numero_a_adivinar:
        print("Intenta con un número más pequeño.")

print("¡Felicidades, ese es el número!")