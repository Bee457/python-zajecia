# Zad 7.6
import itertools
import random

# (a) 0, 1, 0, 1, 0, 1, ...
iter_a = itertools.cycle([0, 1])

# (b) losowy kierunek z ("N", "E", "S", "W")
iter_b = iter(lambda: random.choice(("N", "E", "S", "W")), None)

# (c) 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, ...
iter_c = itertools.cycle(range(7))

import unittest

class TestIterators(unittest.TestCase):

    def test_iter_a(self):
        wynik = []
        for i in range(10):
            wynik.append(next(iter_a))
        self.assertEqual(wynik, [0, 1, 0, 1, 0, 1, 0, 1, 0, 1])

    def test_iter_b(self):
        kierunki = ("N", "E", "S", "W")
        for i in range(20):
            self.assertIn(next(iter_b), kierunki)

    def test_iter_c(self):
        wynik = []
        for i in range(14):
            wynik.append(next(iter_c))
        self.assertEqual(wynik, [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
