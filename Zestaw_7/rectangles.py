# Zad 7.3
from points import Point

class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("niepoprawne wspolrzedne")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return "[{}, {}]".format(self.pt1, self.pt2)

    def __repr__(self):
        return "Rectangle({}, {}, {}, {})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):
        self.pt1 = self.pt1 + Point(x, y)
        self.pt2 = self.pt2 + Point(x, y)
        return self

    def intersection(self, other):
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)
        if x1 >= x2 or y1 >= y2:
            raise ValueError("brak czesci wspolnej")
        return Rectangle(x1, y1, x2, y2)

    def cover(self, other):
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)

    def make4(self):
        srodek = self.center()
        r1 = Rectangle(self.pt1.x, self.pt1.y, srodek.x, srodek.y)
        r2 = Rectangle(srodek.x, self.pt1.y, self.pt2.x, srodek.y)
        r3 = Rectangle(self.pt1.x, srodek.y, srodek.x, self.pt2.y)
        r4 = Rectangle(srodek.x, srodek.y, self.pt2.x, self.pt2.y)
        return (r1, r2, r3, r4)

import unittest

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(0, 0, 4, 2)
        self.r2 = Rectangle(1, 1, 3, 5)
        self.r3 = Rectangle(5, 5, 7, 8)

    def test_init(self):
        with self.assertRaises(ValueError):
            Rectangle(4, 0, 2, 2)
        with self.assertRaises(ValueError):
            Rectangle(0, 5, 2, 2)
        with self.assertRaises(ValueError):
            Rectangle(2, 0, 2, 4)
        with self.assertRaises(ValueError):
            Rectangle(0, 3, 4, 3)

    def test_str(self):
        self.assertEqual(str(self.r1), "[(0, 0), (4, 2)]")
        self.assertEqual(str(self.r2), "[(1, 1), (3, 5)]")

    def test_repr(self):
        self.assertEqual(repr(self.r1), "Rectangle(0, 0, 4, 2)")
        self.assertEqual(repr(self.r2), "Rectangle(1, 1, 3, 5)")

    def test_eq(self):
        self.assertTrue(self.r1 == Rectangle(0, 0, 4, 2))
        self.assertFalse(self.r1 == self.r2)

    def test_ne(self):
        self.assertTrue(self.r1 != self.r2)
        self.assertFalse(self.r1 != Rectangle(0, 0, 4, 2))

    def test_center(self):
        self.assertEqual(self.r1.center(), Point(2.0, 1.0))
        self.assertEqual(self.r2.center(), Point(2.0, 3.0))

    def test_area(self):
        self.assertEqual(self.r1.area(), 8)
        self.assertEqual(self.r2.area(), 8)

    def test_move(self):
        self.r1.move(2, 3)
        self.assertEqual(self.r1, Rectangle(2, 3, 6, 5))
        self.r2.move(-1, -1)
        self.assertEqual(self.r2, Rectangle(0, 0, 2, 4))

    def test_intersection(self):
        self.assertEqual(self.r1.intersection(self.r2), Rectangle(1, 1, 3, 2))
        self.assertEqual(self.r1.intersection(Rectangle(1, 0, 2, 1)), Rectangle(1, 0, 2, 1))
        with self.assertRaises(ValueError):
            self.r1.intersection(self.r3)
        with self.assertRaises(ValueError):
            self.r1.intersection(Rectangle(4, 0, 6, 2))

    def test_cover(self):
        self.assertEqual(self.r1.cover(self.r2), Rectangle(0, 0, 4, 5))
        self.assertEqual(self.r1.cover(self.r3), Rectangle(0, 0, 7, 8))

    def test_make4(self):
        wynik = (
            Rectangle(0, 0, 2.0, 1.0),
            Rectangle(2.0, 0, 4, 1.0),
            Rectangle(0, 1.0, 2.0, 2),
            Rectangle(2.0, 1.0, 4, 2)
        )
        self.assertEqual(self.r1.make4(), wynik)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
