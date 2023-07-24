from random import *

lives = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    lives = 10

if difficulty == 'hard':
    lives = 5

answer = randint(1, 100)

while lives > 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = input("Make a guess: ")
    if int(guess) > answer:
        print("Too high. \nGuess again")
        lives -= 1
    elif int(guess) < answer:
        print("Too low. \nGuess again")
        lives -= 1
    else:
        print("Correct!")
        exit()

print("You Lose!")

