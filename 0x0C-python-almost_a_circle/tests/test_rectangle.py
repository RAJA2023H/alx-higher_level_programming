# test the rectangle class that inherits from Base class
import unittest
from models.rectangle import Rectangle
from models.base import Base


class testrectangle(unittest.TestCase):
    """
    class that test rectangle
    """

    def test_InhertsBase(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_first_id(self):
        """
        test id
        """
        r1 = Rectangle(10, 2)
        r1id = r1.id
        print("---> {}".format(r1id))
        self.assertEqual(r1id, 3)

    def test_second_id(self):
        """ doc"""
        r2 = Rectangle(2, 10)
        r2id = r2.id
        print("---> {}".format(r2id))
        self.assertEqual(r2id, 4)

    def test_third_NOTNONE_id(self):
        """ doc """
        r3 = Rectangle(10, 2, 0, 0, 12)
        r3id = r3.id
        print("---> {}".format(r3id))
        self.assertEqual(r3id, 12)
