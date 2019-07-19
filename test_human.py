__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "Nov 2018"
__email__ = "bilaleluneis@gmail.com"

from unittest import TestCase
from multiple_inheritance import Human, Father, Mother, Son


class TestHuman(TestCase):

    # will run only once before the creation of TestHuman instance
    @classmethod
    def setUpClass(cls) -> None:
        pass

    # will run before ech
    def setUp(self) -> None:
        pass

    def test_sub_instances_are_human(self):
        father = Father()
        mother = Mother()
        son = Son()
        self.assertTrue(isinstance(father, Human))
        self.assertTrue(isinstance(mother, Human))
        self.assertTrue(isinstance(son, Human))
        self.assertTrue(isinstance(mother, Father))

    def tearDown(self) -> None:
        pass

    # will run once only at end after the completion of last Test
    @classmethod
    def tearDownClass(cls) -> None:
        pass
