# -------- OTHER -------- 

# Guesses
guesses = []
play = "yes"

# Top 10
RICHEST_COUNTRIES_ANSWERS = ["Luxembourg", "Macao SAR", "Ireland", "Singapore", 
                    "Qatar", "UAE", "Switzerland", "San Marino", 
                        "United States", "Norway"]

# -------- FUNCTIONS --------

# Welcomes the user and introduces the quiz
def intro():
    # Asks the user their name
    name = input("What is your name? ")

    # Greets the user
    print("Welcome to the quiz, {}.".format(name))
    print("This quiz is about the top 10 richest countries in the world, can you name them?")

# How many attempts the user will be given
def getLives():
    while True:
        lives = input("How many chances do you want? ")
        try:
            lives = int(lives)
            if lives == 0:
                print("Please choose a number higher than 0.")
            if lives >= 0:
                return lives
            else:
                print("Please choose a positive number.")
        except:
            print("That wasn't a number.")

# Checks if the answer already exists in lists, checks previous and correct guesses.
def inList(answer, list):
    if answer in list:
        return True
    else:
        return False

# Checks if the answer is correct
def isCorrect(answer, list):
    if answer in list:
        return True
    else:
        return False


# -------- MAIN CODE --------

intro()   
while play.lower() == "yes":
    score = 0
    lives = getLives()

    if lives == 0:
        getLives()
    while lives >= 1 or lives == 0:
        answer = input("Name one of the top 10 richest countries in the world.\nAnswer here: ")
        if inList(answer, RICHEST_COUNTRIES_ANSWERS):
            # checks if guessed already
            if inList(answer, guesses):
                print("You've guessed that already.")
            else:
                print("Correct!")
                score += 1
                guesses.append(answer)
                print("You have guessed {} of the 10 richest countries. Your score is {}. You have {} chances remaining".format(len(guesses), score, lives))
                if score == 10:
                    break
        else:
            print("Wrong!")
            lives -= 1
            print("You have guessed {} of the 10 richest countries. Your score is {}. You have {} chances remaining.".format(len(guesses), score, lives))
    

    # The end
    if score == 10:
        print("Congrats, you correctly guessed all the countries. Good job!")
    elif lives == 0:
        print("You are out of lives, game over. You had a final score of {}".format(score))
        
    play = input("Would you like to play again? ")