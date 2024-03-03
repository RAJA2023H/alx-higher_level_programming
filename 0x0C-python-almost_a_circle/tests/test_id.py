#test case to check id
import unittest
from models.base import Base
class testBase(unittest.TestCase):
    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
