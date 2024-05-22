# // Others \\
import time
import random

# // Functions \\
def intro():
    print("Hello there, this is a guess the number test.")
    time.sleep(0.5)
    name = input("What is your name? ")
    print("Welcome, {}".format(name))

def question1():
    question1 = input("Guess a number from 1-5: ")
    answer1 = random.randint(1-5)
    if question1 == answer1:
        print("You are correct!")
    else:
        print("You are correct!")
        print(answer1)

# // Main Code \\
intro()
question1()