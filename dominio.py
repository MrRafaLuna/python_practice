correo = input("Ingresa tu dirección de correo electrónico: ")

# Separamos el correo en dos partes
partes = correo.split('@')

if len(partes) != 2:
    print("La dirección de correo electrónico no es válida.")
else:
    print("El dominio de la dirección de correo electrónico es:", partes[1])