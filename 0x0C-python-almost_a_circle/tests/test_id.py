#test case to check id
import unittest
from models.base import Base
class testBase(unittest.TestCase):
    def test_IDNONE(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
    def test_IDNOTNONE(self):
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
    def test_THIRD_ATTRIBUTE(self):
        b3 = Base()
        self.assertEqual(b3.id, 2)
