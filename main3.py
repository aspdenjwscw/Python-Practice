# // Score \\
score = 0

# // Asks the user their name \\
name = input("What is your name? ")

# // Welcoming the user to the quiz \\
print("Welcome to the quiz,", name)
print("This quiz is about Math")
print("There is a scoring system in this quiz, your score is currently 0. If you get a question correct, 1 point will be added to your score.")

# // Questions / Answers \\

# question1
question1 = "What is 56 + 14? "
q1a = "72"
q1b = "70"
q1c = "60"
q1d = "68"

answer1 = input("{}\n A.{} B.{} C.{} D.{} ".format(question1, q1a, q1b, q1c, q1d)).lower()

if answer1 == q1b or answer1 == "b":
    print("Correct!")
    score += 1
    print("1 point has been added to your score, your score is now {}".format(score))

else:
    print("That was not an option!")
    print("Your score has not changed, it is now {}".format(score))

# question2
answer2 = input("What is 50 x 6? ")

if answer2 == "300":
    print("Correct!")
    score += 1
    print("1 point has been added to your score, your score is now {}".format(score))

else:
    print("Incorrect, the answer was 300!")
    print("Your score has not changed, it is now {}".format(score))

# question3
question3 = "What is 36 divided by 3? "
q3a = "13"
q3b = "11"
q3c = "12"
q3d = "14"

answer3 = input("{}\n A.{} B.{} C. {} D. {} ".format(question3, q3a, q3b, q3c, q3d)).lower()
if answer3 == q3c or answer3 == "c":
    print("Correct!")
    score += 1
    print("1 point has been added to your score, your score is now {}".format(score))

else:
    print("Incorrect, the answer was C!")
    print("Your score has not changed, it is now {}".format(score))

# question4
answer4 = input("What is 6 x 7? ")

if answer4 == "42":
    print("Correct!")
    score += 1
    print("1 point has been added to your score, your score is now {}".format(score))

else:
    print("Incorrect, the answer was 42!")
    print("Your score has not changed, it is now {}".format(score))

## // Ending the quiz \\

if score == 4:
    print("Good job {}, your final score was {}! You aced the quiz!".format(name, score))

elif score < 2:
    print("Well, {} your score was {} which isn't good, better luck next time.".format(name, score))

else:
    print("Good job {}, your final score was {}!".format(name, score))
