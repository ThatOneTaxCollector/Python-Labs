
"""
Project Name: Menu-Driven Program

Description:It's a basic nestest menu loop which takes in options for different functions within the program.
    Such as adding and subtracting numbers.
    where the user inputs their choice of numbers and the program outputs the results.

Authors: Braden Gerlach, Braden Gerlach
Date: 6.13.2024

===== Header =====

What used to have a GUI now has a terminal menu.
as shown below.
Menu:
1. Add numbers
2. Subtract numbers
3. Quit

"""

# ===== List of contibuting members =====
# Partner 1: Braden Gerlach
# Partner 2: Braden Gerlach
# It's just me lol

# lab4.py (Driver Program)


import module1
import module2

# the main function
def main():
    while True:
        module1.print_menu()
        choice = module1.get_valid_choice()

        if choice == 1:
            module2.add_numbers()
        elif choice == 2:
            module2.subtract_numbers()
        elif choice == 3:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()