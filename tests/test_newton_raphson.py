import math
import unittest

from src.newton_raphson import newton_raphson

class TestNewtonRaphson(unittest.TestCase):

    def test1(self):
        f = lambda x: math.cos(x) - x
        df = lambda x: -math.sin(x) - 1
        x0 = 1.0
        er = 1e-4
        n = 20
        raiz, error = newton_raphson(f, df, x0, er, n)
        self.assertAlmostEqual(raiz, 0.739085, places=5)
        self.assertLess(error, er)

    def test2(self):
        f = lambda x: x**3 - x - 2
        df = lambda x: 3*x**2 - 1
        x0 = 1.5
        er = 1e-5
        n = 20
        raiz, error = newton_raphson(f, df, x0, er, n)
        self.assertAlmostEqual(raiz, 1.521379, places=5)
        self.assertLess(error, er)

if __name__ == "__main__":
    unittest.main()