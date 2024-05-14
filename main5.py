# // Others \\
import time
import random

play = "yes"
score = 0

QUESTION_FORMAT = "{}\n A. {}\n B. {}\n C. {}\n D. {}\nAnswer here: "
COMMENT_LIST_POSITIVE = ["Good job", "Amazing!", "Keep up the good work.", "That was nice!"]
COMMENT_LIST_NEGATIVE = ["That wasn't good", "Try again.", "You can do better", "Unlucky."]

QUESTIONS = ["How many bones are in an ear? ",
                "Who is the President of the US? ",
                    "How many cat breeds are there? ",
                        "What is the degree of a triangle? ",
                            "How many people are in the world? "]

OPTIONS = [["4", "5", "3", "2"], 
            ["Putin", "Donald Trump", "Joe Biden", "Christopher Luxon"],
                ["73", "65", "15", "127"],
                    ["60", "50", "180", "90"],
                        ["5 billion", "7.5 billion", "7 billion", "8 billion"]]

SHORT_OPTIONS = ["a", "b", "c", "d"]
ANSWERS = [2, 2, 0, 2, 3]

# // Starting the quiz \\
print("")
name = input("What is your name? ")
print("")
print("Welcome to the quiz, {}. This is a general knowledge quiz.".format(name))
print("This quiz has a scoring system, if you get a question correct, 1 point will be awarded.")

# how many attempts they want

while True:
    try:
        tries = input("How many attempts do you want for each question (1-3)? ")
        tries = int(tries)
        print("")
        print("Cool, you will now get {} tries for each question.".format(tries))
        break
    except:
        print("That is not a number.")

## // Questions \\

# beginning the quiz
print("The quiz will begin in 3 seconds.")
time.sleep(3)
print("")

while play == "yes":

    # question 1
    question_attempts1 = tries
    while question_attempts1 > 0:
        print("\nQuestion 1:")
        answer1 = input(QUESTION_FORMAT.format(QUESTIONS[0], OPTIONS[0][0], 
                                                OPTIONS[0][1], OPTIONS[0][2], OPTIONS[0][3])).lower()
        if answer1 == OPTIONS[0][ANSWERS[0]] or answer1 == SHORT_OPTIONS[ANSWERS[0]]:
            print("You are correct!", random.choice(COMMENT_LIST_POSITIVE))
            score += 1
            print("1 point has been added to your score, it is now {}.".format(score))
            break
        elif answer1 == "":
            print("You didn't type anything... but the answer was {}.".format(OPTIONS[0][2]))
            print(random.choice(COMMENT_LIST_NEGATIVE))
        else:
            print("You are incorrect, the answer was {}.".format(OPTIONS[0][2]))
            print(random.choice(COMMENT_LIST_NEGATIVE))
        time.sleep(2.5)
        question_attempts1 -= 1

    # question 2
    question_attempts2 = tries
    while question_attempts2 > 0:
        print("\nQuestion 2:")
        answer2 = input(QUESTION_FORMAT.format(QUESTIONS[1], OPTIONS[1][0],
                                                OPTIONS[1][1], OPTIONS[1][2], OPTIONS[1][3])).lower()
        if answer2 == OPTIONS[1][ANSWERS[1]] or answer2 == SHORT_OPTIONS[ANSWERS[0]]:
            print("You are correct!", random.choice(COMMENT_LIST_POSITIVE))
            score += 1
            print("1 point has been added to your score, it is now {}.".format(score))
            break
        elif answer2 == "":
            print("You didn't type anything... but the answer was {}.".format(OPTIONS[1][2]))
            print(random.choice(COMMENT_LIST_NEGATIVE))
        else:
            print("You are incorrect, the answer was {}.".format(OPTIONS[1][2]))
            print(random.choice(COMMENT_LIST_NEGATIVE))
        time.sleep(2.5)
        question_attempts2 -= 1

    # question 3
    question_attempts3 = tries
    while question_attempts3 > 0:
        print("\nQuestion 2:")
        answer3 = input(QUESTION_FORMAT.format(QUESTIONS[2], OPTIONS[2][0],
                                                OPTIONS[2][1], OPTIONS[2][2], OPTIONS[2][3])).lower()
        if answer3 == OPTIONS[2][ANSWERS[2]] or answer3 == SHORT_OPTIONS[ANSWERS[0]]:
            print("You are correct!", random.choice(COMMENT_LIST_POSITIVE))
            score += 1
            print("1 point has been added to your score, it is now {}.".format(score))
            break
        elif answer3 == "":
            print("You didn't type anything... but the answer was {}.".format(OPTIONS[1][0]))
            print(random.choice(COMMENT_LIST_NEGATIVE))
        else:
            print("You are incorrect, the answer was {}.".format(OPTIONS[2][0]))
            print(random.choice(COMMENT_LIST_NEGATIVE))
        time.sleep(2.5)
        question_attempts3 -= 1