
# author: Bilal El Uneis
# since: April 2018
# bilaleluneis@gmail.com


class Methods:

    number_of_instances = 0  # this is a class level property

    # initializer with default values (constructor)
    def __init__(self, method_name="anonymous", method_return_type="void"):
        self.method_name = method_name
        self.method_return_type = method_return_type
        type(self).number_of_instances += 1  # this is how to access class level var inside init

    # I am guessing this is like a destructor in other languages like C++
    def __del__(self):
        type(self).number_of_instances -= 1

    # this is an instance method, every instance method has first argument as self
    def update_method_name(self, new_name):
        self.method_name = new_name

    # this is a class level method
    @classmethod
    def get_class_number_of_instances(cls):
        return cls.number_of_instances

    # a static method
    @staticmethod
    def is_valid_return_type(method_return_type):
        if method_return_type in ["void", "int", "String"]:
            return True
        else:
            return False


# start of running code
if __name__ == "__main__":
    print("current number of instances = {}".format(Methods.get_class_number_of_instances()))
    instance_1 = Methods()
    instance_2 = Methods(method_return_type="float")  # need to use argument name if you are passing only one param
    instance_3 = Methods("awesome", "String")
    print("current number of instances = {}".format(Methods.get_class_number_of_instances()))
    instance_1.update_method_name("instance_1")
    print("instance_1 method name is updated to {}".format(instance_1.method_name))
    del instance_1  # this will call the __del__ (destructor)
    print("current number of instances = {}".format(Methods.get_class_number_of_instances()))
    valid_return_type = Methods.is_valid_return_type(instance_2.method_return_type)
    print("instance_2 method return type is valid: {}".format(valid_return_type))
    valid_return_type = Methods.is_valid_return_type(instance_3.method_return_type)
    print("instance_3 method return type is valid: {}".format(valid_return_type))
    del instance_2
    del instance_3
    print("current number of instances = {}".format(Methods.get_class_number_of_instances()))
