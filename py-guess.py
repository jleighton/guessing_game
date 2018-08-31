import random
number = random.randrange(1,50)
print (number)
guess = int(input("Guess a number...."))

while guess != number:
    if guess > number:
        guess = int(input("Lower...."))
        
    if guess < number:
        guess = int(input("Higher...."))
        
print("Bingo!")