nombre = input("Ingresa tu nombre: ")
while "*" in nombre:
    print("ERROR: No puedes utilizar asteriscos (*) en el nombre.")
    nombre = input("Ingresa tu nombre: ")

fecha_nacimiento = input("Ingresa tu fecha de nacimiento (dd/mm/aaaa): ")
while "*" in fecha_nacimiento:
    print("ERROR: No puedes utilizar asteriscos (*) en la fecha de nacimiento.")
    fecha_nacimiento = input("Ingresa tu fecha de nacimiento (dd/mm/aaaa): ")

direccion = input("Ingresa tu dirección: ")
while "*" in direccion:
    print("ERROR: No puedes utilizar asteriscos (*) en la dirección.")
    direccion = input("Ingresa tu dirección: ")

meta_profesional = input("Ingresa tu meta profesional: ")
while "*" in meta_profesional:
    print("ERROR: No puedes utilizar asteriscos (*) en la meta profesional.")
    meta_profesional = input("Ingresa tu meta profesional: ")

print("Información del usuario:")
print("Nombre: ", nombre)
print("Fecha de nacimiento: ", fecha_nacimiento)
print("Dirección: ", direccion)
print("Meta profesional: ", meta_profesional)