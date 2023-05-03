palabra = input("Ingresa una palabra: ")

# Revertir la palabra
revertida = palabra[::-1]

# Verificar si es un palíndromo
if palabra == revertida:
    print(palabra, "es un palíndromo")
else:
    print(palabra, "no es un palíndromo")