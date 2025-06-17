import random
from random import randint
import art #get ascii art from art.py file

numbers = randint(0, 101)  #choose random numbers from 0 to 100
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def easy_attempt(): #run easy function

    print("You have 10 attempts remaining to guess the number.")
    attempt = 10
    while attempt > 0:
        guess = int(input("Make a guess:"))
        if guess < numbers:
            print("TOO LOW!!")
        if guess > numbers:
            print("Too HIGH!")
        if guess == numbers:
            print(f"You got it! The answer was {numbers}")
            break
        else:
            attempt -= 1 #decrement of attempt 
    if attempt == 0:
        print("Out of attempts!")


def hard_attempt(): #run hard function
    print("You have 5 attempts remaining to guess the number.")

    attempt = 5
    while attempt > 0:
        guess = int(input("Make a guess:"))
        if guess < numbers:
            print("TOO LOW!!")
        if guess > numbers:
            print("Too HIGH!")
        if guess == numbers:
            print(f"You got it! The answer was {numbers}")
            break
        else:
            attempt -= 1 #decrement of attempt 
    if attempt == 0:
        print("Out of attempts!")




if choice == "easy": #if user choose easy then call easy function 
    easy_attempt()

if choice == "hard": #if user choose hard then call hard function 
    hard_attempt()



