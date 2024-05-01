# Asks the user their name
name = input("What is your name? ")

# Welcoming them to the Quiz
print("Welcome to the quiz", name)
print("This quiz is about New Zealand!")

# Questions / Answers
answer1 = input("True or false: Is Wellington the capital city of NZ? ")

if (answer1.lower() == "true"):
    print("You are correct!")
else:
    print("You are incorrect!")

answer2 = input("True or false: Is Christchurch the biggest city in NZ? ")

if (answer2.lower() == "false"):
    print("You are correct! ")
else:
    print("You are incorrect! ")

answer3 = input("How many more sheep than humans are there in NZ? \n A: 20 Million \n B: 15 Million \n C: 22 Million: \n Choose A, B or C: ")

if (answer3.lower() == "a"):
    print("You are correct!")
else:
    print("You are incorrect!")

# Thanking them for playing the quiz
print("Thank you for playing the quiz!")