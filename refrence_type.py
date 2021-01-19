import unittest

__author__ = "Bilal El Uneis"
__since__ = "August 2020"
__email__ = "bilaleluneis@gmail.com"


class A:

    def __init__(self) -> None:
        pass

    @property
    def id(self) -> int:
        return id(self)


class RefrenceTypeTests(unittest.TestCase):

    def test_refrence(self) -> None:
        a = A()
        b = a
        self.assertTrue(a.id == b.id)  # a and b point to same memory address

        original_memory_id = a.id
        a = A()  # a is now pointing to new memory address

        self.assertTrue(b.id == original_memory_id)  # b is still pointing to a's old memory address
        self.assertTrue(a.id != b.id)


if __name__ == '__main__':
    unittest.main()
