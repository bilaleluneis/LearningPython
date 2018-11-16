__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "Nov 2018"
__email__ = "bilaleluneis@gmail.com"

"""
Examples showing how to prevent direct class instance creation,
but allow inheritance and creation of instance of sub class!
"""


# this class can't be instantiated
class CantInstantiate(object):

    def __init__(self):
        print("__init__ called in CantInstantiate !")

    # override the __new__ operator to prevent creating instance of this class
    def __new__(cls, *args, **kwargs):
        if cls is CantInstantiate:
            raise TypeError("CantInstantiate __new__ Not allowed to create instance !")
        return object.__new__(cls)


# CantInstantiate can be inherited and subclass can be instantiated
class SubClass(CantInstantiate):

    def __init__(self):
        super().__init__()
        print("__init__ called in SubClass !")


# using composition and trying to instantiate CantInstantiate, will expose the behaviour
class CompositionNotAllowed(object):

    def __init__(self):
        self.__instance = CantInstantiate()
        print("__init__ called in CompositionNotAllowed")


def main():
    SubClass()
    CompositionNotAllowed()


# start of running code
if __name__ == "__main__":
    main()
