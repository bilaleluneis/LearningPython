__author__ = "Bilal El Uneis"
__since__ = "September 2018"
__email__ = "bilaleluneis@gmail.com"


class Human:

    """
    this is class level property that is shared among all instances of this class.
    each instance will have access to this one shared property.
    also notice that you have two _ before it. that makes it a private access property,
    which means subclasses and the outside don't have direct access to it.

    """
    __population = 0

    def __init__(self, name="Un-named"):
        # to access class level property , use the class name or cls
        Human.__population = Human.__population + 1
        """
        this is instance level property , each instance of this class will have its own
        also notice the one _ , this makes this property a protected access level
        which allows you to access from here and also from subclass, but not visible to the outside
        
        """
        self._name = name
        print("new Instance of Human Created!")

    def get_name(self):
        return self._name

    @classmethod
    def get_population(cls):
        return cls.__population


class HumanSecondGen(Human):
    def __init__(self):
        super().__init__()

    def set_name(self, a_name):
        self._name = a_name


def main():
    print("population number is {}".format(Human.get_population()))
    bilal = HumanSecondGen()
    bilal.set_name("Bilal")
    print("name is {}".format(bilal.get_name()))
    print("population is {}".format(bilal.get_population()))


# start of running code
if __name__ == "__main__":
    main()
