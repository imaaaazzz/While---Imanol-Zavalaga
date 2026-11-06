acumulador = 0
numero = int(input("Ingrese un número entero: "))
mayor = numero
menor = numero

while acumulador < 9:
    numero = int(input("Ingrese otro número entero: "))

    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

    acumulador += 1

print("El mayor número ingresado es:", mayor)
print("El menor número ingresado es:", menor)

