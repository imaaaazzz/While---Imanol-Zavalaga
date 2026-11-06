suma = 0
contador_negativos = 0
respuesta = ""
producto = 1

while respuesta != "Listo":
    numeros = float(input("Ingrese un número: "))
    if numeros > 0:
        suma += numeros
    elif numeros < 0:
        producto *= numeros
        contador_negativos += 1
    
    respuesta = str(input("¿Desea ingresar otro número? (Escriba 'Listo' para finalizar): "))

print("La suma de los números positivos ingresados es:", suma)

if contador_negativos > 0:
    print("El producto de los negativos es:", producto)
else:
    print("No se ingresaron números negativos.")