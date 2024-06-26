class Drink:

    # constructor for drink class
    def __init__(self, name, type, size, price):
        self.__name = name
        self.__type = type
        self.__size = size
        self.__price = price

    # getters for drink class
    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_size(self):
        return self.__size

    def get_price(self):
        return self.__price