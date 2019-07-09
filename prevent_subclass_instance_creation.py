
__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "Nov 2018"
__email__ = "bilaleluneis@gmail.com"

"""
Examples showing how to prevent a sub class from been instantiated
"""


class SubClassCantBeInstantiated(object):

    def __init__(self):
        print("__init__ SubClassCantBeInstantiated called!")

    # override the __new__ operator to prevent creating instance of any Subclass inheriting this class
    def __new__(cls, *args, **kwargs):
        if cls is SubClassCantBeInstantiated:
            return object.__new__(cls)
        else:
            raise TypeError("Not allowed to create instance!")


# can't create instance of subclass
class SubClass(SubClassCantBeInstantiated):

    def __init__(self):
        super().__init__()
        print("__init__ SubClass called!")


def main():
    SubClassCantBeInstantiated()
    SubClass()


# start of running code
if __name__ == "__main__":
    main()
