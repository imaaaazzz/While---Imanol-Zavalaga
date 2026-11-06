numero = float(input("Ingrese un número: "))
contador_positivos = 0
suma = 0
numeros_negativos = 0
contador_negativos = 0
respuesta = ""
mayor = numero


while respuesta != "Listo":
    numero = float(input("Ingrese un número: "))

    if numero > 0:
        suma += numero
        contador_positivos += 1

    if numero > 0 and numero > mayor:
        mayor = numero

    if numero < 0:
        numeros_negativos += numero
        contador_negativos += 1

    respuesta = str(input("¿Desea ingresar otro número? (Escriba 'Listo' para finalizar): "))

print("El mayor número ingresado es:", mayor)

print ("La suma de los numeros positivos es:", suma)

print ("La cantidad de numeros negativos ingresados es:", contador_negativos)

promedio_positivos = (suma / contador_positivos)
print("El promedio de los números positivos es:", promedio_positivos)

porcentaje_negativos = (contador_negativos / (contador_positivos + contador_negativos)) * 100
print("El porcentaje de números negativos es:", int(porcentaje_negativos),"%")
