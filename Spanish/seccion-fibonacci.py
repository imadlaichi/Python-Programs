n = int(input("¿Cuántos números de la sucesión de Fibonacci quieres saber? "))
fibo_ant1, fibo_ant2 = 1, 1
for i in range(n):
    print(fibo_ant1)
    fibo_ant1, fibo_ant2 = fibo_ant2, fibo_ant1 + fibo_ant2
