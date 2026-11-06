acumulador = 0
bandera =False
suma = 0
while bandera != True:
    
    numero = int(input("Ingrese un número entero: "))
    suma += numero
    
    acumulador += 1
    if acumulador >= 5:
       respuesta = str(input("Quieres seguir ingresando números? (Escriba 'Listo' para finalizar): "))
       if respuesta == "Listo":
           bandera = True
       else:
           bandera = False
    elif acumulador < 5:
        bandera = False

promedio = suma / acumulador
print("El promedio de los números ingresados es:", promedio)
print("La suma de los números ingresados es:", suma)