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


class Son(Father, Mother):
    def __init__(self):
        super(Son, self).__init__()
        gender = self.get_gender()
        print("Son is of " + gender)


class Daughter(Mother, Father):
    def __init__(self):
        super(Daughter, self).__init__()
        gender = self.get_gender()
        print("Daughter is of " + gender)


# start of running code

son = Son()
daughter = Daughter()
