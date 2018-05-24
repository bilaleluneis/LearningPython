

__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "April 2018"
__email__ = "bilaleluneis@gmail.com"


"""
so access modifiers in Python are not really enforced, more like a hint.
applying access modifiers before class name doesnt do anything when it comes
to creating instance. no warning , no error.

now at least in PyCharm IDE .. if you try to access a protected method, you get a warning.
if you try to access private method you get unresolved attribute reference and if you run the code
you get error at runtime.
"""


class PublicClass:

    _protected_var = None

    __private_var = None

    public_var = None

    dummy_message = "method called!"

    def _protected_method(self):
        print("protected {}".format(self.dummy_message))

    def __private_method(self):
        print("private {}".format(self.dummy_message))

    def public_method(self):
        print("public {}".format(self.dummy_message))


class _ProtectedClass:

    _protected_var = None

    __private_var = None

    public_var = None

    dummy_message = "method called!"

    def _protected_method(self):
        print("protected {}".format(self.dummy_message))

    def __private_method(self):
        print("private {}".format(self.dummy_message))

    def public_method(self):
        print("public {}".format(self.dummy_message))


class __PrivateClass:

    _protected_var = None

    __private_var = None

    public_var = None

    dummy_message = "method called!"

    def _protected_method(self):
        print("protected {}".format(self.dummy_message))

    def __private_method(self):
        print("private {}".format(self.dummy_message))

    def public_method(self):
        print("public {}".format(self.dummy_message))


# start of running code
if __name__ == "__main__":

    # creating instances of the classes with diff access modifiers, no issues.
    # but I wonder if I was outside this file and try to create instance of protected or private class
    # if I still don't get warning or error!
    publicInstance = PublicClass()
    protectedInstance = _ProtectedClass()
    privateInstance = __PrivateClass()

    # accessing methods on those instances, notice you get warning on protected and error on private.
    # I am starting to think the classes would have similar behaviour if we try to instantiate from outside
    # this file !!
    publicInstance.public_method()
    publicInstance._protected_method()  # notice you get warning
    # uncomment bellow line and see the error !
    # publicInstance.__private_method()

