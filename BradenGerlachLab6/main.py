"""
Program: Object-Oriented Coffee Menu/Lab6
Authors: Braden Gerlach
Date: 6.13.2024

Description:
This Program displays a menu of coffee drinks and does so in an object-oriented way.
It does this by taking in a list of drinks stored in the menu.py file that is think imported in this file, main.

This Program takes in no user input but can be configured to display whatever the user wants.

"""

# imports
from Drink import Drink
from Menu import Menu

# main function
def main():
    menu = Menu.get_menu()

    for drink in menu:
        print(f"{drink.get_name()} - {drink.get_type()} - {drink.get_size()} - ${drink.get_price()}")


if __name__ == "__main__":
    main()