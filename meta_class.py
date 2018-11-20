__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "Nov 2018"
__email__ = "bilaleluneis@gmail.com"

"""
Meta Classes are the blue print for classes just like classes are blue print for types instantiated from them.
they allow to set class capabilities.
bellow is example:
Meta Class To prevent inheritance of Class when used.
"""


class CantInheritFrom(type):
    def __new__(mcs, name, bases, attr):
        type_list: [] = [type(x) for x in bases]
        for _type in type_list:
            if _type is CantInheritFrom:
                raise RuntimeError("You cannot subclass a Final class")
        return super(CantInheritFrom, mcs).__new__(mcs, name, bases, attr)


"""
Actual Classes that will use Meta Classes to adjust class capabilities
"""


class FinalClass(metaclass=CantInheritFrom):
    def __init__(self):
        print("__init__ FinalClass")

# uncomment class bellow to see error
# class A(FinalClass):
#     def __init__(self):
#         super().__init__()
#         print("__init__ A")


def main():
    FinalClass()
    # A()


# start of running code
if __name__ == "__main__":
    main()
