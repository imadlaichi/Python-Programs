n = int(input("Enter the number whose factorial you want to know: "))
i = 1
while n >= 1:
    i *= n
    n -= 1
print(i)
