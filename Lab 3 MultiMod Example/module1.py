# module1.py (Partner 1's Module)

# Partner 1: Braden Gerlach

def print_menu():
    print("\n\nPress one of the following options: ")
    print("+++++ Menu +++++")
    print("1. Add numbers")
    print("2. Subtract numbers")
    print("3. Quit")
    print("+++++++++++++++")

# More error catching
def get_valid_choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please enter a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")
