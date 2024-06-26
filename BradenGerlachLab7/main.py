"""
Title: Coffee Menu
Author: Braden Gerlach
Date: 6/13/2024
Version: 1.1

Description:
- A simple command-line application that allows users to search for different types of coffee drinks.

Features:
- Custom database query to fetch coffees based on search type
- User input validation
- Error handling for fetching coffees from the database
- Loop for performing multiple queries
- Thank you message at the end
- Help message explaining how to use the application set to 'help'

input("Enter the type of coffee you're looking for (shot, breve, or drip.): ").strip().lower()
output("The coffee menu for your search type:")

"""

from Name import Name


def main():
    print("\n===============================")
    print("~ Welcome to the Coffee Menu ~")
    print("===============================\n")
    print_help_message()

    while True:
        # Ask the user to enter search terms
        search_type = get_search_type_input()

        if search_type in ['exit', 'quit']:
            break

        flavor = get_flavor_input()

        # Fetch the coffees from the database
        try:
            coffees = Name.readNames(search_type, flavor)  # Pass both search_type and flavor
            if coffees:
                # Print the coffees
                print_coffees(coffees)
            else:
                print("No coffees found for the provided search type and flavor.")
        except Exception as e:
            print(f"An error occurred while fetching coffees: {str(e)}")

        # Ask if the user wants to perform another query
        choice = get_yes_no_input("\nDo you want to perform another query? (y/n): ")
        if choice != 'y':
            break

    print("\n======================================")
    print("~ Thank you for using the Coffee Menu ~")
    print("======================================\n")


def get_search_type_input():
    """
    Prompt the user to enter the type of coffee they're looking for.
    Validates the input and returns the search type.
    """
    while True:
        search_type = input("Enter the type of coffee you're looking for (shot, breve, or drip): ").strip().lower()
        if search_type == 'help':
            print_help_message()
            continue
        elif search_type in ['exit', 'quit']:
            return search_type
        elif not search_type:
            print("Please enter a valid search type.")
            continue
        return search_type


def get_flavor_input():
    """
    Prompt the user to enter the flavor of coffee they prefer.
    Returns the flavor input.
    """
    flavor = input("Enter the flavor of coffee you prefer (bitter, sweet, mellow): ").strip().lower()
    return flavor

def print_help_message():
    """
    Print the help message explaining how to use the Coffee Menu application.
    """
    print("\n~ Coffee Menu Help ~")
    print("To search for coffee, enter the type of coffee you're looking for (shot, breve, or drip).")
    print("You can also type 'help' at any time to display this help message.")
    print("To exit the program, type 'exit' or 'quit'.\n")


def get_yes_no_input(prompt):
    """
    Prompt the user with a yes or no question and return their response.
    Validates the input and returns 'y' or 'n'.
    """
    while True:
        choice = input(prompt).strip().lower()
        if choice == 'help':
            print_help_message()
            continue
        elif choice in ['exit', 'quit']:
            return choice
        elif choice not in ['yes', 'y', 'no', 'n']:
            print("Please enter 'yes' or 'y' for yes, 'no' or 'n' for no.")
            continue
        return choice[:1]  # Return only the first character ('y' or 'n')


def print_coffees(coffees):
    """
    Print the list of available coffees.
    """
    print("\n===============================")
    print("~ Available Coffees ~:")
    print("===============================\n")
    for coffee in coffees:
        print(f"{coffee['Name']}: {coffee['Description']}")
    print("===============================")


if __name__ == "__main__":
    main()
