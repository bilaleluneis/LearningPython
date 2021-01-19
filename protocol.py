from abc import abstractmethod
from unittest import TestCase, main

from typing_extensions import Protocol, runtime_checkable, T, Type, Literal

__author__ = "Bilal El Uneis"
__since__ = "May 2020"
__email__ = "bilaleluneis@gmail.com"


@runtime_checkable
class Collection(Protocol[T]):

    @abstractmethod
    def __iter__(self) -> 'Collection[T]': ...

    @abstractmethod
    def __contains__(self, item: T) -> bool: ...

    @abstractmethod
    def __len__(self) -> int: ...

    @abstractmethod
    def __getitem__(self, index: int) -> T: ...


@runtime_checkable
class Iterable(Collection[T], Protocol):

    @abstractmethod
    def __next__(self) -> T: ...


class List(Iterable[T]):

    def __init__(self, *args: T) -> None:
        self.__content: list = [e for e in args] if len(args) else []

    def __iter__(self) -> Collection[T]:
        return self.__content

    def __next__(self) -> T:
        try:
            return self.__content.pop()
        except IndexError:
            raise StopIteration

    def __contains__(self, item: T) -> bool:
        return item in self.__content

    def __len__(self) -> int:
        return len(self.__content)

    # TODO: check if index is valid
    def __getitem__(self, index: int) -> T:
        return self.__content[index]


class Set(Iterable[T]):
    def __init__(self, *args: T) -> None:
        self.__content: set = {e for e in args} if len(args) else {}

    def __iter__(self) -> Collection[T]:
        return self.__content.__iter__()

    def __next__(self) -> T:
        try:
            return self.__content.pop()
        except IndexError:
            raise StopIteration

    def __contains__(self, item: T) -> bool:
        return item in self.__content

    def __len__(self) -> int:
        return len(self.__content)

    # TODO: check if index is valid
    def __getitem__(self, index: int) -> T:
        return self.__content[index]


def getinstance(typ: Type[T], collection_type: Literal["list", "set"], *elements: T) -> Iterable[T]:
    return List[typ](*elements) if collection_type == "list" else Set[typ](*elements)


class ProtocolTests(TestCase):

    def test_create_protocol_instance(self) -> None:
        with self.assertRaises(TypeError):
            Iterable[float]()

        with self.assertRaises(TypeError):
            Collection[int]()

    def test_create_list(self) -> None:
        i: Iterable[int] = [1, 2, 3, 4]
        self.assertTrue(len(i) == 4)

        l1: Iterable[int] = List[int]()
        self.assertTrue(len(l1) == 0)

        l2: Iterable[int] = List[int](1, 2, 3)
        self.assertTrue(len(l2) == 3)

    def test_create_set(self) -> None:
        s1: Iterable[int] = {1, 2, 3}
        self.assertTrue(len(s1) == 3)

        s2: Iterable[int] = Set[int]()
        self.assertTrue(len(s2) == 0)

        s3: Iterable[int] = Set[int](1, 2, 3)
        self.assertTrue(len(s3) == 3)

    def test_create_iterable(self) -> None:
        i1: Iterable[int] = getinstance(int, "list", 1, 2, 3, 4)
        self.assertTrue(isinstance(i1, List))


if __name__ == '__main__':
    main()
