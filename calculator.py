# Import
import time

# Functions
def subtract(x, y):
    return x - y

def add(x, y):
    return x + y

def divide(x, y):
    return x / y

def multiply(x, y):
    return x * y

print("\nWhat calculation would you like to do?")
print("1. Subtraction")
print("2. Addition")
print("3. Division")
print("4. Multiplication")

while True:
    choice = input("Enter choice (1, 2, 3, 4): ")
    print("")

    if choice in ('1', '2', '3','4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print("Answer:", num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '2':
            print("Answer:", num1, "+", num2, "=", add(num1, num2))
        
        elif choice == '3':
            print("Answer:", num1, "/", num2, "=", divide(num1, num2))

        elif choice == '4':
            print("Answer:", num1, "*", num2, "=", multiply(num1, num2))

        print("")
        another_calculation = input("Do you want to do another calculation (Yes / No): ").lower()
        if another_calculation == "no":
            break

    else:
        print("Invalid Input.")