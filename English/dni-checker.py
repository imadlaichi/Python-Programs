incomplete_dni = int(input("What are the numbers in your incomplete DNI?: "))
remainder = incomplete_dni % 23

letters = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", 'L', "C", "K", "E"]

complete_dni = letters[remainder]
print(str(incomplete_dni) + str(complete_dni))
