# module2.py (Partner 2's Module)

# Partner 2: Braden Gerlach

def add_numbers():
    # I do not wish to concatenate this function
    while True:
        try:
            print("\n\nEnter two numbers to add.")
            print("+++++++++++++++++++++++++++++++++++++++++")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("And now the second number: "))
            print("+++++++++++++++++++++++++++++++++++++++++")
            result = num1 + num2
            print("Result: {:.2f}".format(result))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def subtract_numbers():
    # I do not wish to concatenate this function
    while True:
        try:
            print("\n\nEnter two numbers to subtract.")
            print("+++++++++++++++++++++++++++++++++++++++++")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("+++++++++++++++++++++++++++++++++++++++++")
            result = num1 - num2
            print("Result: {:.2f}".format(result))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")