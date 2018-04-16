
# author: Bilal El Uneis
# since: April 2018
# bilaleluneis@gmail.com


class PropertyDecorator:

    def __init__(self, initial_name):
        self.__property_name = initial_name  # notice __property_name, that is how you define private with _ _

    # in python @ is called decorator , which is similar to annotations in Java / Kotlin
    @property
    def property_name(self):  # this is a property getter
        return self.__property_name

    @property_name.setter  # property setter
    def property_name(self, new_name):
        self.__property_name = new_name

    @property_name.deleter  # this gets called when you do del property_name, to delete it
    def property_name(self):
        self.__property_name = None


# start of running code
if __name__ == "__main__":

    example = PropertyDecorator("initial name")
    print(example.property_name)  # this will call the getter method for the property
    example.property_name = "new name"  # this will call the setter method for the property
    print(example.property_name)
    del example.property_name
    print(example.property_name)
