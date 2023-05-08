# Vehicle Class

class Automobile:
    def __init__(self, make, model_id, mileage, price):
        self.__make = make
        self.__model_id = model_id
        self.__mileage = mileage
        self.__price = price

    def set_make(self, make):
        self.__make = make

    def set_model_id(self, model_id):
        self.__model_id = model_id

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    def get_make(self):
        return self.__make

    def get_model_id(self):
        return self.__model_id

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

    def __str__(self):
        result = '\n============================= '+\
                  '\nMake: ' + self.get_make() + \
                 '\nModel ID:'+ str(self.get_model_id()) + \
                 '\nMileage: ' + self.get_mileage() + \
                 '\nPrice: ' + self.get_price() + \
                 '\n============================= '
        return result

