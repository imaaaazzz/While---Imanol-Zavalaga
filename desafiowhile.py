print ("--- Recolección de Datos ---")
genero = ("Masculino", "Femenino", "Otro")
tecnologia = ("IA", "RV/RA", "IOT")
contador = 0
mens = 0
not_ia = 0

mayor = 0
tecnologia_mayor = ""
nombre_mayor = ""

while contador < 5: 
    nombre = input("Ingrese un nombre: ")

    while nombre == "":
        print("Error, el nombre no puede estar vacío.")
        nombre = input("Ingrese un nombre: ")

    edad = int(input("Ingrese la edad: "))

    while edad < 18 or edad > 90:
        print("Edad incorrecta.")
        edad = int(input("Ingrese la edad: "))

    print("Seleccione el género:")
    print("1. Masculino")
    print("2. Femenino")
    print("3. Otro")
    genero = input("Ingrese el género: ")
    while genero not in ["1", "2", "3"] :
        print("Género incorrecto.")
        genero = input("Ingrese el género: ")

    if genero == "1":
        genero = "Masculino"
    elif genero == "2":
        genero = "Femenino"
    elif genero == "3":
        genero = "Otro"

    print("Seleccione la tecnología de interés:")
    print("1. Inteligencia Artificial (IA)")
    print("2. Realidad Virtual/Aumentada (RV/RA)")
    print("3. Internet de las Cosas (IOT)")
    tecnologia = input("Ingrese la tecnología de interés: ")
    
    while tecnologia not in ["1", "2", "3"] and tecnologia not in ["IA", "RV/RA", "IOT"]:
        print("Tecnología incorrecta.")
        tecnologia = input("Ingrese la tecnología de interés: ")

    if tecnologia == "1":
        tecnologia = "Inteligencia Artificial (IA)"
    elif tecnologia == "2":
        tecnologia = "Realidad Virtual/Aumentada (RV/RA)"
    elif tecnologia == "3":
        tecnologia = "Internet de las Cosas (IOT)"     


    if genero == "Masculino" and edad > mayor: 
        mayor = edad
        nombre_mayor = nombre
        tecnologia_mayor = tecnologia

     
    if genero != "Femenino" and tecnologia != "Inteligencia Artificial (IA)" and edad >= 33 and edad <= 40:
        not_ia += 1

    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Género: {genero}")
    print(f"Tecnología de interés: {tecnologia}")

    if genero == "Masculino" and (tecnologia == "Inteligencia Artificial (IA)" or tecnologia == "Internet de las Cosas (IOT)") and edad >= 25 and edad <= 50:
            mens += 1

    contador += 1

 
porcentaje = (not_ia / contador) * 100

print(f"Cantidad de hombres entre 25 y 50 años interesados en IA o IOT: {mens}")
print(f"Nombre del hombre de mayor edad: {nombre_mayor}")
print(f"Edad del hombre de mayor edad: {mayor}")
print(f"Tecnología de interés del hombre de mayor edad: {tecnologia_mayor}")
print(f"Porcentaje de personas que no son mujeres, no están interesadas en IA y tienen entre 33 y 40 años: {porcentaje:.2f}%")