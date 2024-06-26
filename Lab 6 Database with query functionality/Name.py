from Database import get_coffees

# Reads the names from the custom database based on the search type and returns
# them as a list of dictionaries. It with throw and error if an error occurs while fetching.
class Name:
    @staticmethod
    def readNames(search_type, flavor=None):
        try:
            coffees = get_coffees(search_type, flavor)
            return coffees
        except Exception as e:
            raise Exception(f"An error occurred while fetching coffees: {str(e)}")