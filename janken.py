import random

def jugar():
    opciones = ["piedra", "papel", "tijera"]
    maquina = random.choice(opciones)
    jugador = input("Elige piedra, papel o tijera: ").lower()

    if jugador not in opciones:
        print("Esa no es una opción válida. Inténtalo de nuevo.")
        jugar()
    else:
        print("La máquina eligió: " + maquina)
        if jugador == maquina:
            print("¡Empate!")
        elif jugador == "piedra" and maquina == "tijera":
            print("¡Ganaste!")
        elif jugador == "papel" and maquina == "piedra":
            print("¡Ganaste!")
        elif jugador == "tijera" and maquina == "papel":
            print("¡Ganaste!")
        else:
            print("¡Perdiste!")

jugar()