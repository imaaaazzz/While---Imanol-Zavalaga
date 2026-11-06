acumulador = 0
suma = 0

while acumulador < 5:
    numeros = float(input("Ingrese un número: "))
    suma += numeros
    acumulador += 1

print("La suma de los números ingresados es:", suma)
promedio = (suma / acumulador) 
print("El promedio de los números ingresados es:", promedio)