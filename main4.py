# // Others \\
import time
import sys
play = "yes"
score = 0
QUESTION_FORMAT = "{}\n A. {}\n B. {}\n C. {}\n D. {}\nAnswer here: "

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
for i in range(10):
    print("The quiz will begin in 3 seconds.")
    sys.stdout.write("\033[F")
time.sleep(3)
print("")

while play == "yes":
    
    # question 1
    question_attempts1 = tries
    while question_attempts1 > 0:
        print("\nQuestion 1:")
        question1 = "How many bones are in an ear?"
        q1a = "4"
        q1b = "5"
        q1c = "3"
        q1d = "2"
        answer1 = input(QUESTION_FORMAT.format(question1, q1a, q1b, q1c, q1d)).lower()
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

    # question 2
    question_attempts2 = tries
    while question_attempts2 > 0:
        print("\nQuestion 2:")
        question2 = "Aureolin is a shade of what color?"
        q2a = "Blue"
        q2b = "Green"
        q2c = "Orange"
        q2d = "Yellow"
        answer2 = input(QUESTION_FORMAT.format(question2, q2a, q2b, q2c, q2d)).lower()
        if answer2 == q2d.lower() or answer2 == "d":
            print("You are correct!")
            score += 1
            print("1 point has been added to your score, it is now {}.".format(score))
            break
        elif answer2 == "":
            print("You didn't type anything... but the answer was {}.".format(q2d))
        else:
            print("You are incorrect, the answer was {}.".format(q2d))
        time.sleep(2.5)
        question_attempts2 -= 1

    # question 3
    question_attempts3 = tries
    while question_attempts3 > 0:
        print("\nQuestion 3:")
        question3 = "How many faces does a Dodecahedron have? "
        q3a = "14"
        q3b = "12"
        q3c = "10"
        q3d = "8"
        answer3 = input(QUESTION_FORMAT.format(question3, q3a, q3b, q3c, q3d)).lower()
        if answer3 == q3b.lower() or answer2 == "b":
            print("You are correct!")
            score += 1
            print("1 point has been added to your score, it is now {}.".format(score))
            break
        elif answer3 == "":
            print("You didn't type anything... but the answer was {}.".format(q3d))
        else:
            print("You are incorrect, the answer was {}.".format(q3d))
        time.sleep(2.5)
        question_attempts3 -= 1
     
    # // Ending the quiz \\
    
    # telling them their final score
    print("Well done {}. You had a final score of {}.".format(name, score))
    score = 0
    # replay
    play = input("Do you want to play again? ").lower()