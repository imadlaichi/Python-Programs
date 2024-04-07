numero = int(input("Introduce el número que deseas saber si es primo o no: "))

if numero > 1:
    for i in range(2, numero):
        if (numero % i) == 0:
            print(numero, "no es un número primo")
            break
    else:
        print(numero, "es un número primo")
else:
    print(numero, "no es un número primo")
