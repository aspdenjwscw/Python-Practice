# Score
score = 0

# Asks the user their name
name = input("What is your name? ")

# Welcoming them to the Quiz
print("Welcome to the quiz,", name)
print("This quiz is about New Zealand!")

# Questions / Answers
answer1 = input("True or false: Is Wellington the capital city of NZ? ")

if (answer1.lower() == "true"):
    print("You are correct!")
    score+=1
    print("+1 Point has been added to your score, your score is now", score)
else:
    print("You are incorrect!")
    print("The answer is True")
    print("No points have been added to your score, your score is now", score)

answer2 = input("True or false: Is Christchurch the biggest city in NZ? ")

if (answer2.lower() == "false"):
    print("You are correct! ")
    score+=1
    print("+1 Point has been added to your score, your score is now", score)
else:
    print("You are incorrect! ")
    print("The answer is True")
    print("No points have been added to your score, your score is now", score)

answer3 = input("How many more sheep than humans are there in NZ? \n A: 20 Million \n B: 15 Million \n C: 22 Million: \n Choose A, B or C: ")

if (answer3.lower() == "a"):
    print("You are correct!")
    score+=1
    print("+1 Point has been added to your score, your score is now", score)
else:
    print("You are incorrect!")
    print("The answer is A")
    print("No points have been added to your score, your score is now", score)

answer4 = input("Who is the current Prime Minister of NZ? ")

if (answer4.lower() == "christopher luxon"):
    print("You are correct!")
    score+=1
    print("+1 Point has been added to your score, your score is now", score)
else:
    print("You are incorrect!")
    print("The answer is Christopher Luxon")
    print("No points have been added to your score, your score is now", score)

answer5 = input("New Zealand’s Waikato River cascades down what “H” waterfall, just north of Taupo? ")

if (answer5.lower() == "huka falls"):
    print("You are correct!")
    score+=1
    print("+1 Point has been added to your score, your score is now", score)
else:
    print("You are incorrect!")
    print("The answer is Huka Falls")
    print("No points have been added to your score, your score is now", score)

answer6 = input("What’s the fruity name of a flightless bird that lives in New Zealand? ")

if (answer6.lower() == "kiwi"):
    print("You are correct!")
    score+=1
    print("+1 Point has been added to your score, your score is now", score)
else:
    print("You are incorrect!")
    print("The answer is Kiwi")
    print("No points have been added to your score, your score is now", score)

answer7 = input("Wendy Jarland in New Zealand holds the title of having the world's largest collection of paraphernalia related to what back-of-the-alphabet safari mammal? ")

if (answer7.lower() == "zebra"):
    print("You are correct!")
    score+=1
    print("+1 Point has been added to your score, your score is now", score)
else:
    print("You are incorrect!")
    print("The answer is Zebra")
    print("No points have been added to your score, your score is now", score)

answer8 = input("As of 2020, how many female prime ministers has New Zealand had? ")

if (answer8.lower() == "3"):
    print("You are correct!")
    score+=1
    print("+1 Point has been added to your score, your score is now", score)
else:
    print("You are incorrect!")
    print("The answer is 3")
    print("No points have been added to your score, your score is now", score)

if score == 5:
    print("You aced the quiz with a score of 3, great job!")

else:
    print("Your final score was",score,"good job!")

# Thanking them for playing the quiz
print("Thank you for playing the quiz!")