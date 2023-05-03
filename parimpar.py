numero = int(input("Ingresa un número entre 1 y 1000: "))

if numero < 1 or numero > 1000:

    print("El número ingresado no está en el rango válido.")

elif numero % 2 == 0:

    print("El número ingresado es par.")

else:
    
    print("El número ingresado es impar.")