__author__ = "Bilal El Uneis"
__since__ = "Dec 2019"
__email__ = "bilaleluneis@gmail.com"


class CanAddAttributesToInstance:
    def __init__(self) -> None:
        pass


class CantAddAttributesToInstance:
    __slots__ = ()

    def __init__(self) -> None:
        pass


class AllowOnlyAttribToInstance:
    __slots__ = ('name', 'age')

    def __init__(self) -> None:
        pass


def main() -> None:
    v1 = AllowOnlyAttribToInstance()
    v1.name = 'Bilal'
    print(v1.name)
    v1.age = 38
    print(v1.age)
    v1.__slots__ = ('name', 'age', 'height')
    v1.height = 3000
    print(v1.height)


# start of running code
if __name__ == "__main__":
    main()
