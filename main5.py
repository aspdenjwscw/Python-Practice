# // Others \\
import time
import random

play = "yes"
score = 0

QUESTION_FORMAT = "{}\n A. {}\n B. {}\n C. {}\n D. {}\nAnswer here: "
COMMENT_LIST_POSITIVE = ["Good job!", "Amazing!", "Keep up the good work.", "That was nice!"]
COMMENT_LIST_NEGATIVE = ["That wasn't good, try again.", "Incorrect, try again.", "You can do better, try again!", "Unlucky, try again."]

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
    score = 0
    
    for i in range(len(QUESTIONS)):
        question_attempts = tries
        while question_attempts > 0:
            answer = input(QUESTION_FORMAT.format(QUESTIONS[i], OPTIONS[i][0],
                                                    OPTIONS[i][1], OPTIONS[i][2], OPTIONS[i][3])).lower()
            if answer == OPTIONS[i][ANSWERS[i]].lower() or answer == SHORT_OPTIONS[ANSWERS[i]]:
                print("You are correct!", random.choice(COMMENT_LIST_POSITIVE))
                score += 1
                print("1 point has been added to your score, it is now {}.".format(score))
                break
            elif answer == "":
                print("Not sure?")
            elif answer in SHORT_OPTIONS or answer in OPTIONS[i]:
                print("Wrong!, the answer was {}".format(i))
                print(random.choice(COMMENT_LIST_NEGATIVE))
            else:
                print("That was not an option.")
            question_attempts -= 1
            if question_attempts == 0:
                print("You ran out of attempts, you will be moved onto the next question.")
                break


    # // Ending the quiz \\

    # indicating the user of their final score

    if score == 5:
        print("Wow {}!! Good job, you aced the quiz with a score of {}.".format(name, score))

    elif score < 5:
        print("Well done, {}, you had a final score of {}.".format(name, score))

    if score < 2:
        print("Uh, you didn't do that well to be honest {}. Maybe try again, your score of {} was not that good.".format(name, score))

    # replay
        
    play = input("Would you like to play again (yes / no)? ").lower()