
# author: Bilal El Uneis
# since: April 2018
# bilaleluneis@gmail.com


class Human:
    def __init__(self):
        print("new Instance of Human created!")

    def get_gender(self):
        return "No Gender Specified!"


class Male(Human):
    def __init__(self):
        print("New Instance of Male Created!")
        super(Male, self).__init__()

    def get_gender(self):
        return "Male Gender!"


class Female(Human):
    def __init__(self):
        print("New Instance of Female Created!")
        super(Female, self).__init__()

    def get_gender(self):
        return "Female Gender"


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
