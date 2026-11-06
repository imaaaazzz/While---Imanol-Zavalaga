acumulador = 0
numero = 1

while numero <= 10:
    if numero % 2 == 0:
        acumulador = acumulador + numero

    numero += 1
    print(acumulador)
    
    