n = int(input("Introduce el número del cual deseas conocer su factorial: "))
i = 1
while n >= 1:
    i *= n
    n -= 1
print(i)
