__author__ = "Bilal El Uneis"
__since__ = "June 2018"
__email__ = "bilaleluneis@gmail.com"


class Vehicle:

    def __init__(self):
        self.start = False
        self.stop = True
        self.turnDirection = None
        print("Vehicle instance created!")

    def type(self):
        print("Vehicle")


class Car(Vehicle):

    def __init__(self):
        super().__init__()
        self.gearNumbers = 3
        print("Car instance created!")

    def type(self):
        print("Car")


class SportsCar(Car):

    def __init__(self):
        super().__init__()
        self.gearNumbers = 6
        print("Sports Car instance created!")

    def type(self):
        print("Sports Car")


# start of running code
if __name__ == "__main__":

    carOne = Car()
    carOne.type()
    print("number of gears on the car is {}\n".format(carOne.gearNumbers))

    sportsCar = SportsCar()
    sportsCar.type()
    print("number of gears on the sports car is {}\n".format(sportsCar.gearNumbers))

    carOne.type()
    print("number of gears on the car is {}\n".format(carOne.gearNumbers))

    # creating collection of vehicles
    print("Looping through collection ")
    vehicles = [carOne, sportsCar]
    for v in vehicles:
        v.type()





