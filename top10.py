# -------- LISTS -------- 

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
            if lives >= 0:
                return lives
            else:
                print("Please choose a positive number.")
        except:
            print("That wasn't a number.")

# Checks if the answer is correct
def isCorrect(answer, list):
    if answer in list:
        return True
    else:
        return False


# -------- MAIN CODE --------

intro()
lives = getLives()

score = 0
while lives >= 0:
    answer = input("Name one of the top 10 richest countries in the world.\nAnswer here: ")

    if isCorrect(answer, RICHEST_COUNTRIES_ANSWERS):
        score += 1
        print("You are correct, good job!")
        print("1 point has been added to your score, it is now {}".format(score))
    else:
        lives -= 1
        print("You are wrong.")
        print("1 of your lives has been removed, you now have {} lives.".format(lives))

print("You are out of lives, game over.")