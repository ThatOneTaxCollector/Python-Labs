"""
Project Name: Food Order Calculator/ Lab 3
Description: A program that calculates the total cost of food items ordered.
Authors: Braden Gerlach
Date: 6.13.2024

===== Header =====
Calculator that adds user made food items and their prices and display a receipt.\
user inputs(cost of food, and name of food item) represented as food_item and price.
===== Changes Made =====
-Gutted the entire project to make it look cleaner and more readable.
"""
def main():
    user_wants_to_continue = True
    # globals
    while user_wants_to_continue:
        total_cost = 0
        food_items = []
        food_prices = []

        print("Welcome to the Food Order Calculator!")
        # mainloop with breaks for user input and error handling
        while True:
            food_item = input("Enter the food item (or 'done' to finish): ")
            if food_item.lower() == 'done':
                break

            price = input("Enter the price for {}: $".format(food_item))
            while True:
                try:
                    price = float(price)
                    if price < 0:
                        raise ValueError
                    break
                except ValueError:
                    price = input("Please enter a valid positive price for {}: $".format(food_item))

            food_items.append(food_item)
            food_prices.append(price)
            total_cost += price

        print("\nTotal Cost: ${:.2f}".format(total_cost))
        print("Tip Suggestions:")
        for tip_percentage in [10, 15, 20]:
            tip_amount = total_cost * tip_percentage / 100
            print("{}% Tip: ${:.2f}".format(tip_percentage, tip_amount))

        # some more user input cleaning and error handling
        while True:
            user_input = input("Do you want to run the program again? (yes/no): ")
            if user_input.lower() == 'yes' or user_input.lower() == 'no':
                break
            else:
                print("Please enter 'yes' to run the program again or 'no' to exit.")

        user_wants_to_continue = user_input.lower() == 'yes'

if __name__ == "__main__":
    main()