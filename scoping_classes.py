__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "Nov 2018"
__email__ = "bilaleluneis@gmail.com"


class ScopedClasses:

    # meta class to prevent inheritance of classes.
    class _CantInherit(type):
        def __new__(mcs, name, bases, classdict):
            for b in bases:
                if isinstance(b, ScopedClasses._CantInherit):
                    raise TypeError("type '{0}' is not an acceptable base type".format(b.__name__))
            return type.__new__(mcs, name, bases, dict(classdict))

    class PublicClass:
        def __init__(self):
            print("__init__ PublicClass !")

    """
    To make class protected, I will allow only inheritance of it , 
    but not allow direct creation of instance from it. this class 
    will be visible from the outside also.
    """

    class _ProtectedClass:
        def __init__(self):
            print("__init__ _ProtectedClass !")

        # override the __new__ operator to prevent creating instance of this class
        def __new__(cls, *args, **kwargs):
            if cls is ScopedClasses._ProtectedClass:
                raise TypeError("_ProtectedClass __new__ Not allowed to create instance !")
            return object.__new__(cls)

    class PublicClassInheritingProtected(_ProtectedClass):
        def __init__(self):
            super().__init__()
            print("__init__ PublicClassInheritingProtected !")

    """
        To make class private added __ before name.
        This class will not be visible from the outside,
        and can only be inherited from inside this file.
    """

    class __PrivateClass:
        def __init__(self):
            print("__init__ __PrivateClass !")

    class PublicClassInheritPrivate(__PrivateClass):
        def __init__(self):
            super().__init__()
            print("__init__ PublicClassInheritPrivate !")


"""
This is one way to Scope Classes to Public, Private and Protected.
bellow you will notice you can't even access the __PrivateClass and 
you can't instantiate direct instance of _ProtectedClass
"""


def main():
    ScopedClasses.PublicClass()
    ScopedClasses.PublicClassInheritingProtected()
    ScopedClasses.PublicClassInheritPrivate()


# start of running code
if __name__ == "__main__":
    main()
