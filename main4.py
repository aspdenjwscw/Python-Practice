# // Others \\
import time
import sys
play = "yes"
score = 0

# // Starting the quiz \\
name = input("What is your name? ")
print("Welcome to the quiz, {}. This is a general knowledge quiz.".format(name))
print("This quiz has a scoring system, if you get a question correct, 1 point will be awarded.")

# how many attempts they want

while True:
    try:
        tries = input("How many attempts do you want for each question (1-3)? ")
        tries = int(tries)
        print("Cool, you will now get {} tries for each question.".format(tries))
        break
    except:
        print("That is not a number.")

## // Questions \\

# beginning the quiz
for i in range(10):
    print("The quiz will begin in 5 seconds.")
    sys.stdout.write("\033[F")
time.sleep(5)

# question 1

while play == "yes":

    question_attempts1 = tries
    while question_attempts1 > 0:
        print("\nQuestion 1:")
        question1 = "How many bones are in an ear?"
        q1a = "4"
        q1b = "5"
        q1c = "3"
        q1d = "2"
        answer1 = input("{}\n A. {}\n B. {}\n C. {}\n D. {}\nAnswer here: ".format(question1, q1a, q1b, q1c, q1d)).lower()
        if answer1 == q1c or answer1 == "c":
            print("You are correct!")
            score += 1
            print("1 point has been added to your score, it is now {}.".format(score))
            break
        elif answer1 == "":
            print("You didn't type anything... but the answer was {}.".format(q1c))
        else:
            print("You are incorrect, the answer was {}.".format(q1c))
        time.sleep(2.5)
        question_attempts1 -= 1

    question_attempts2 = tries
    while question_attempts2 > 0:
        print("\nQuestion 2:")
        question2 = "Aureolin is a shade of what color?"
        q2a = "Blue"
        q2b = "Green"
        q2c = "Orange"
        q2d = "Yellow"
        answer2 = input("{}\n A. {}\n B. {}\n C. {}\n D. {}\nAnswer here: ".format(question2, q2a, q2b, q2c, q2d)).lower()
        if answer2 == q2d.lower() or answer2 == "d":
            print("You are correct!")
            score += 1
            print("1 point has been added to your score, it is now {}.".format(score))
            break
        elif answer1 == "":
            print("You didn't type anything... but the answer was {}.".format(q2d))
        else:
            print("You are incorrect, the answer was {}.".format(q2d))
        time.sleep(2.5)
        question_attempts2 -= 1
    # // Ending the quiz \\
    
    # telling them their final score
    print("Well done {}. You had a final score of {}.".format(name, score))
    score = 0
    # replay
    play = input("Do you want to play again? ").lower()