# Zad 6.2
from math import sqrt

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __hash__(self):
        return hash((self.x, self.y))

import unittest

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(3, 4)
        self.p2 = Point(1, 2)
        self.zero = Point(0, 0)

    def test_str(self):
        self.assertEqual(str(self.p1), "(3, 4)")
        self.assertEqual(str(self.zero), "(0, 0)")

    def test_repr(self):
        self.assertEqual(repr(self.p1), "Point(3, 4)")
        self.assertEqual(repr(self.p2), "Point(1, 2)")

    def test_eq(self):
        self.assertTrue(self.p1 == Point(3, 4))
        self.assertFalse(self.p1 == self.p2)

    def test_ne(self):
        self.assertTrue(self.p1 != self.p2)
        self.assertFalse(self.p1 != Point(3, 4))

    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Point(4, 6))
        self.assertEqual(self.p1 + Point(-3, -4), self.zero)

    def test_sub(self):
        self.assertEqual(self.p1 - self.p2, Point(2, 2))
        self.assertEqual(self.p1 - self.p1, self.zero)

    def test_mul(self):
        self.assertEqual(self.p1 * self.p2, 11)
        self.assertEqual(self.p1 * self.zero, 0)

    def test_cross(self):
        self.assertEqual(self.p1.cross(self.p2), 2)
        self.assertEqual(self.p1.cross(self.p1), 0)

    def test_length(self):
        self.assertEqual(self.p1.length(), 5.0)
        self.assertEqual(self.zero.length(), 0.0)

    def test_hash(self):
        self.assertEqual(hash(self.p1), hash(Point(3, 4)))
        self.assertNotEqual(hash(self.p1), hash(self.p2))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
