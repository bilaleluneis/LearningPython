
# author: Bilal El Uneis
# since: April 2018
# bilaleluneis@gmail.com

"""
want to try to use this which i saw in youtube video
super().__init__(properties)
and this when doing super for 2 types that were inherited
Father.__init__(self, properties)
Mother.__init__(self, properties)
"""

class Human:
    def __init__(self, gender=None):
        print("new Instance of Human created! with gender = {}".format(gender))


class Male(Human):
    def __init__(self):
        super().__init__("Male")


class Female(Human):
    def __init__(self):
        super().__init__("Female")


class Father(Male):
    def __init__(self):
        super(Father, self).__init__()


class Mother(Female):
    def __init__(self):
        super(Mother, self).__init__()


# the reason gender is Male here is because Son instance will look first at get_gender()
# from Father class as it is first in the sequence of multiple inheritance
class Son(Father, Mother):
    def __init__(self):
        super(Son, self).__init__()
        gender = self.get_gender()
        print("Son is of " + gender)


# the reason gender is Female here is because Daughter instance will look first at get_gender()
# from Mother class as it is first in the sequence of multiple inheritance
class Daughter(Mother, Father):
    def __init__(self):
        super(Daughter, self).__init__()
        gender = self.get_gender()
        print("Daughter is of " + gender)


# start of running code
if __name__ == "__main__":
    son = Son()
    daughter = Daughter()
