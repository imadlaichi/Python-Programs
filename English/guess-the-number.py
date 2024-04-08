import random
number = random.randint(1, 100)
guess = 0
print(number)
attempts = 0
while number != guess:
    attempts += 1
    guess = int(input("Guess the number I've picked from 1-100: "))
    if guess > number:
        print("The number I've picked is smaller than", guess)
    if guess < number:
        print("The number I've picked is greater than", guess)
       
if number == guess:
    print("Correct! You took", attempts, "attempts to guess the number.")
