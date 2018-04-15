
# author: Bilal El Uneis
# since: April 2018
# bilaleluneis@gmail.com


class SimpleInit:

    """
     - looks like I can have only one init method in the class.
     - I can set default values for properties in init and any methods.
     - I don't need to declare properties at top level of class !!
     - the properties are available to the instance of the class, even though not declared at top level.
     - this is really interesting, run the main via debugger. notice how you are able to pass
       anything (any type) to property_one and two .. I think this is because var name is nothing
       but a pointer to memory and there is no such thing as compile , the code is interpreted at
       runtime and only then the type in that memory location is determined?!
    """
    def __init__(self, property_one, property_two, property_three="some default value"):
        self.property_one = property_one
        self.property_two = property_two
        self.property_three = property_three


# start of running code
if __name__ == "__main__":
    example1 = SimpleInit("1", 2)
    example2 = SimpleInit(1, "2")
    example3 = SimpleInit(example1, example2, "just WOW!!")
    print(example3.property_three)  # you can access properties this way !
    print("End of Program!")

