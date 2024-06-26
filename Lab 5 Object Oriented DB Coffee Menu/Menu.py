
# import

from Drink import Drink

# menu database
class Menu:
    @staticmethod
    def get_menu():
        drinks = [
            {"name": "Espresso", "type": "Strong", "size": "Small", "price": 2.50},
            {"name": "Latte", "type": "Mild", "size": "Medium", "price": 3.50},
            {"name": "Cappuccino", "type": "Strong", "size": "Medium", "price": 3.00},
            {"name": "Mocha", "type": "Sweet", "size": "Large", "price": 4.00},
            {"name": "Americano", "type": "Medium", "size": "Large", "price": 3.00}
        ]
        return [Drink(drink["name"], drink["type"], drink["size"], drink["price"]) for drink in drinks]