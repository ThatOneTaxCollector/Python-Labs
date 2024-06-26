
def get_coffees(search_type, flavor=None):
    coffees = {
        "shot": [
            {"Name": "Espresso", "Description": "A strong, bold coffee drink.", "Flavor": "Bitter"},
            {"Name": "Latte", "Description": "A milky coffee drink with a steamer on top.", "Flavor": "Mellow"},
            {"Name": "Cappuccino", "Description": "A milky coffee drink with a thick layer on top.",
             "Flavor": "Mellow"},
            {"Name": "Mocha", "Description": "A coffee drink with espresso, milk, and chocolate sauce.",
             "Flavor": "Sweet"},
            {"Name": "Late Night", "Description": "A strong coffee drink brewed late at night.", "Flavor": "Bitter"}
        ],
        "breve": [
            {"Name": "Cold Brew",
             "Description": "Coffee that's been brewed cold with a unhealthy dash of half and half.",
             "Flavor": "Bitter"},
            {"Name": "Breve Pumpkin Spice Latte", "Description": "A pumpkin spice-flavored Breve.",
             "Flavor": "Sweet"},
            {"Name": "Iced Breve Latte", "Description": "Like an Iced Latte but worse for the knees.",
             "Flavor": "Sweet"},
            {"Name": "Cappuccino", "Description": "A cappuccino coffee drink with half and half instead of milk.",
             "Flavor": "Mellow"},
            {"Name": "Just Half and Half", "Description": "It's just half and half.", "Flavor": "Mellow"}
        ],
        "drip": [
            {"Name": "Iced Drip", "Description": "Drip coffee that's been brewed and then cooled over ice.",
             "Flavor": "Bitter"},
            {"Name": "Pour Over", "Description": "Drip hot water that's been poured over coffee grounds.",
             "Flavor": "Bitter"},
            {"Name": "Pinkerton's Delight", "Description": "A classic drip coffee drink bombed with milk.",
             "Flavor": "Sweet"},
            {"Name": "Creamed Coffee, Drip", "Description": "A classic drip coffee drink with cream.",
             "Flavor": "Mellow"},
            {"Name": "Sad Office Black Coffee", "Description": "A classic drip coffee from a dirty Keurig machine.",
             "Flavor": "Bitter"}
        ]
    }

    filtered_coffees = [coffee for coffee in coffees.get(search_type, []) if
                        flavor is None or coffee.get("Flavor", "").lower() == flavor.lower()]

    return filtered_coffees
