
print("-- INGRESO DE PERSONA -- ")


apellido = input("Ingrese su apellido: ")

while apellido == "":
    print("Error, el apellido no puede estar vacío.")
    apellido = input("Ingrese su apellido: ")

edad = int(input("Ingrese su edad: "))

while edad < 18 or edad > 90:
    print("Edad incorrecta.")
    edad = int(input("Ingrese su edad: "))

estado_civil = input("Ingrese su estado civil (soltero, casado, divorciado, viudo/a): ")

legajo = int(input("Ingrese su legajo: "))

while legajo < 1000 or legajo > 9999:
    print("Legajo incorrecto.")
    legajo = int(input("Ingrese su legajo: "))

print ("Apellido:", apellido)
print ("Edad:", edad)
print ("Estado civil:", estado_civil)
print ("Legajo:", legajo)