import sys

__author__ = "Bilal El Uneis"
__since__ = "Jan 2019"
__email__ = "bilaleluneis@gmail.com"


class Const(object):
    """
    Modification to Original code from Python Cookbook by David Ascher and Alex Martelli.
    the code was modified from original python 2 support to python 3.7 support.
    """

    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const({})".format(name))
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            raise self.ConstError("Can't unbind const({})".format(name))
        raise NameError(name)


sys.modules[__name__] = Const()
