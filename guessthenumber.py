import random

AFFIRMATIONS = ["Alright!", "Cool!", "Sweet!", "Splendid!", "M'kay!", "Sounds good.", "Perfect.", "Okie dokie!"]
def intro():
    global name
    name = input("What is your name? ")
    print("Welcome to the number guessing quiz, {}.".format(name))

def numguess():
    global number
    while True:
        maxamount = input("What is the maximum number you would like to have? ")
        try:
            maxamount = int(maxamount)
            if maxamount > 1000000:
                print("Please choose a lower number.")
            else:
                print(random.choice(AFFIRMATIONS), "Your maximum number is {}".format(maxamount))
                break
        except:
            print("That wasn't a number.")
    
    while True:
        minamount = input("What is the minimum number you would like to have? ")
        try:
            minamount = int(minamount)
            if minamount > maxamount:
                print("Please choose a number lower than {}".format(maxamount))
            else:
                print(random.choice(AFFIRMATIONS), "Your minimum number is {}".format(minamount))
                break
        except:
            print("That was not a number.")
    number = random.randint(minamount, maxamount)

def guessing():
    global number
    global won
    global numofguesses
    while True:    
        guess = input("What number would you like to guess? ")
        try:
            guess = int(guess)
            break
        except:
            print("That wasn't a number.")
            numofguesses += 1
    if guess == number:
        print("You are correct, good job! That took you {} guesses.".format(numofguesses))
        numofguesses += 1
        won = True
    else:
        if guess > number:
            print("Try a lower number.")
            numofguesses += 1
        else:
            print("Try a higher number.")
            numofguesses += 1

numofguesses = 0
won = False
intro()
numguess()
guessing()
while won == False:
    guessing()
