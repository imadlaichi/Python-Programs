n = int(input("How many numbers of the Fibonacci sequence do you want to know? "))
fibo_ant1, fibo_ant2 = 1, 1
for i in range(n):
    print(fibo_ant1)
    fibo_ant1, fibo_ant2 = fibo_ant2, fibo_ant1 + fibo_ant2
