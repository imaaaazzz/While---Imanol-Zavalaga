acumulador = 0
respuesta = ""
suma = 0

while respuesta != "Listo":
    numeros = float(input("Ingrese un número: "))
    suma += numeros
    acumulador += 1
    respuesta = str(input("Ingrese 'Listo' para finalizar o presione Enter para continuar: "))

promedio = (suma / acumulador)
print("La suma de los números ingresados es:", suma)    
print("El promedio de los números ingresados es:", promedio)