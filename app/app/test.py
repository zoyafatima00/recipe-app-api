"""
sample test
"""

from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add(3, 4)
        self.assertEqual(res, 7)

    def test_subtract(self):
        res = calc.subtract(15, 10)
        self.assertEqual(res, 5)
