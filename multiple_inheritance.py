
# author: Bilal El Uneis
# since: July 2018
# bilaleluneis@gmail.com


class Human:
    def __init__(self):
        self.__gender = None

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value


class Mother(Human):
    def __init__(self):
        super().__init__()
        self.gender = "F"


class Father(Human):
    def __init__(self):
        super().__init__()
        self.gender = "M"


class Son(Father, Mother):
    def __init__(self):
        super().__init__()  # when doing this call, it looks like Mother init gets called first, then Father
        # or you can init super like bellow, then you have control on the order of super class init calls
        # Father.__init__(self)
        # Mother.__init__(self)


# start of running code
if __name__ == "__main__":
    son = Son()
    print("{}".format(son.gender))
