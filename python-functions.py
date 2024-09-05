"""
Question 1. The Calculator App
Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

Task 1: Create functions for each arithmetic operation.
"""
def sum():
    return a + b

def subtract():
    return a - b

def multiply():
    return a * b

def divide():
    return a / b







"""
Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
"""


while True:
    try:
        a = int(input("Type the first number: "))
        b = int(input("Type the second number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    try:
        operation = int(input("Enter the operation number (1/2/3/4): "))
        if operation in [1, 2, 3, 4]:
            break
        else:
            print("Invalid operation. Please choose a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def sum():
    return a + b

def subtract():
    return a - b

def multiply():
    return a * b

def divide():
    if b != 0:
        return a / b
    else:
        return "Error: Can not divide by zero"

if operation == 1:
    print("The result is:", sum())
elif operation == 2:
    print("The result is:", subtract())
elif operation == 3:
    print("The result is:", multiply())
elif operation == 4:
    print("The result is:", divide())






"""
Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.
"""
while True:
    try:
        a = int(input("Type the first number: "))
        b = int(input("Type the second number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    try:
        operation = int(input("Enter the operation number (1/2/3/4): "))
        if operation in [1, 2, 3, 4]:
            break
        else:
            print("Invalid operation. Please choose a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def sum():
    return a + b

def subtract():
    return a - b

def multiply():
    return a * b

def divide():
    try: a / b
    except ZeroDivisionError as e:
        print("Error: Can not divide by zero")

if operation == 1:
    print("The result is:", sum())
elif operation == 2:
    print("The result is:", subtract())
elif operation == 3:
    print("The result is:", multiply())
elif operation == 4:
    print("The result is:", divide())






"""
Question 2. The Shopping List Maker
Objective: The aim of this assignment is to create a program that helps users make a shopping list.

Task 1: Write a function that lets the user add items to a list.
"""


def shopping_list():
    user_list = ""
    while True:
        item = input("Enter an item to add to the list or 'done' to finish: ")
        if item.lower() == "done":
            break
        user_list += item + "\n"
    print("Shopping List:")
    print(user_list)

shopping_list()





"""
Task 2: Include a function to remove items from the list.
"""

def shopping_list():
    user_list = []
    while True:
        item = input("Enter an item to add to the list or 'done' to finish: ")
        if item.lower() == "done":
            break
        user_list.append(item)

    print("Shopping List:")
    for i, item in enumerate(user_list, 1):
        print(f"{i}. {item}")

    while True:
        remove_item = input("Do you want to remove an item from the list? (yes/no): ")
        if remove_item.lower() == "yes":
            item_number = int(input("Enter the number of the item to remove: "))
            try:
                del user_list[item_number - 1]
                print("Item removed. Here is the updated list:")
                for i, item in enumerate(user_list, 1):
                    print(f"{i}. {item}")
            except IndexError:
                print("Invalid item number. Please try again.")
        elif remove_item.lower() == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

shopping_list()






"""
Task 3: Add a function that prints out the entire list in a formatted way.
"""

def shopping_list():
    user_list = []
    while True:
        item = input("Enter an item to add to the list or 'done' to finish: ")
        if item.lower() == "done":
            break
        user_list.append(item)

    print("Shopping List:")
    for i, item in enumerate(user_list, 1):
        print(f"{i}. {item}")

    while True:
        remove_item = input("Do you want to remove an item from the list? (yes/no): ")
        if remove_item.lower() == "yes":
            item_number = int(input("Enter the number of the item to remove: "))
            try:
                del user_list[item_number - 1]
                print("Item removed. Here is the updated list:")
                for i, item in enumerate(user_list, 1):
                    print(f"{i}. {item}")
            except IndexError:
                print("Invalid item number. Please try again.")
        elif remove_item.lower() == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    print("Final Shopping List:")
    for i, item in enumerate(user_list, 1):
        print(f"{i}. {item}")

shopping_list()
