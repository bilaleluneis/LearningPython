__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "Nov 2018"
__email__ = "bilaleluneis@gmail.com"

"""
Examples showing different ways to prevent class instance creation
"""


class InstanceNotAllowed(object):

    def __init__(self, delay: float = 0.5):
        self.__delay = delay

    # override the __new__ operator to prevent creating instance of Timer
    def __new__(cls, *args, **kwargs):
        if cls is InstanceNotAllowed:
            raise TypeError("Not allowed to create instance of Timer !")
        return object.__new__(cls)


# can create instance of subclass
class InstanceNotAllowedSubClass(InstanceNotAllowed):

    def __init__(self):
        super().__init__()
        print("InstanceNotAllowedSubClass created!")


def main():
    InstanceNotAllowedSubClass()
    InstanceNotAllowed()


# start of running code
if __name__ == "__main__":
    main()
