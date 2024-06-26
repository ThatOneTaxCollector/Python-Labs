"""
Program: Coffee Menu/Lab5
Authors: Braden Gerlach
Date: 6.13.2024

Description:
This program allows users to interact with a coffee menu through a terminal user interface (TUI).
Users can list all coffee drinks, view details of a specific coffee drink, add new coffee drinks, edit existing ones,
delete coffee drinks, and exit the program.

The menu takes in user input such as price, type, milk,
 flavor, and topping and stores them in a dictionary.

"""

# Global dictionary to store coffee drink data that can be edited by the user.
coffee_menu = {
    "Latte": {"price": 5.00, "type": "Espresso-based", "milk": "Steamed milk", "flavor": "Vanilla", "topping": "Whipped cream"},
    "Cappuccino": {"price": 5.00, "type": "Espresso-based", "milk": "Foamed milk", "flavor": "Hazelnut", "topping": "Cocoa powder"},
    "Americano": {"price": 4.50, "type": "Espresso-based", "milk": "None", "flavor": "None", "topping": "None"},
    "Mocha": {"price": 5.50, "type": "Espresso-based", "milk": "Steamed milk", "flavor": "Chocolate", "topping": "Whipped cream"}
}

def coffee_menu_display():

    # Coffee Menu header

    coffee_Menu = "=======~Coffee Menu~=======\n\n"
    for drink, details in coffee_menu.items():
        coffee_Menu += f"{drink} - ${details['price']:.2f}\n"

    # Command Menu

    cmdmenu_str = "\n=======<Command MENU>=======\n\n"
    cmdmenu_str += "# list - List all coffee drinks\n"
    cmdmenu_str += "# show - Show a coffee drink\n"
    cmdmenu_str += "# add - Add a coffee drink\n"
    cmdmenu_str += "# edit - Edit a coffee drink\n"
    cmdmenu_str += "# del - Delete a coffee drink\n"
    cmdmenu_str += "# exit - Exit\n"

    return coffee_Menu + cmdmenu_str

# list function
def list_coffee_drinks():
    if len(coffee_menu) == 0:
        print("There are no coffee drinks in the menu.")
    else:
        coffee_list = "Coffee Drink List\n\n"
        for idx, drink in enumerate(coffee_menu.keys(), start=1):
            coffee_list += f"{idx}. {drink}\n"
        print(coffee_list)

# edit function
def add_edit_coffee_drink(mode):
    drink_name = input("Enter the name of the coffee drink: ")
    drink_name = drink_name.capitalize()
    if mode == "add" and drink_name in coffee_menu:
        print(f"{drink_name} is already a coffee drink in our menu.")
        return
    elif mode == "edit" and drink_name not in coffee_menu:
        print(f"{drink_name} doesn't exist as a coffee drink yet.")
        return

# Input menu for added coffee drinks

    price = float(input("Enter the price of the coffee drink: "))
    drink_type = input("Enter the type of the coffee drink (e.g., Espresso-based): ")
    milk = input("Enter the milk used in the coffee drink (e.g., Steamed milk): ")
    flavor = input("Enter the flavor of the coffee drink (e.g., Vanilla): ")
    topping = input("Enter the topping of the coffee drink (e.g., Whipped cream): ")

    coffee_drink = {"price": price, "type": drink_type, "milk": milk, "flavor": flavor, "topping": topping}
    coffee_menu[drink_name] = coffee_drink

    if mode == "add":
        print("Your new coffee drink has been added.")
    elif mode == "edit":
        print("Your coffee drink has been updated.")
    else:
        print("Something went wrong. Please try again.")

# delete function
def delete_coffee_drink():
    drink_name = input("Enter the name of the coffee drink you want to delete: ")
    drink_name = drink_name.capitalize()
    if drink_name in coffee_menu:
        del coffee_menu[drink_name]
        print(f"{drink_name} has been removed from the coffee menu.")
    else:
        print(f"{drink_name} is not in our coffee menu.")

# show function
def show_coffee_drink():
    drink_name = input("Enter the name of the coffee drink you want to view: ")
    drink_name = drink_name.capitalize()
    if drink_name in coffee_menu:
        details = f"{drink_name}\n\n"
        details += f"Price: ${coffee_menu[drink_name]['price']:.2f}\n"
        details += f"Type: {coffee_menu[drink_name]['type']}\n"
        details += f"Milk: {coffee_menu[drink_name]['milk']}\n"
        details += f"Flavor: {coffee_menu[drink_name]['flavor']}\n"
        details += f"Topping: {coffee_menu[drink_name]['topping']}\n"
        print(details)

# main function
def main():
    while True:
        command = input("Enter a command (list, show, add, edit, del, exit): ")
        if command:
            command = command.lower()
            if command == "list":
                list_coffee_drinks()
            elif command == "show":
                show_coffee_drink()
            elif command == "add":
                add_edit_coffee_drink(mode="add")
            elif command == "edit":
                add_edit_coffee_drink(mode="edit")
            elif command == "del":
                delete_coffee_drink()
            elif command == "exit":
                break
            else:
                print("Not a valid command. Please try again.")
        print(coffee_menu_display())

    print("Thanks for using our Coffee Menu!")

if __name__ == "__main__":
    main()
