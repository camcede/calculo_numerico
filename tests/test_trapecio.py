import math
import unittest
from src.trapecio import trapecio

class TestTrapecio(unittest.TestCase):

    def test1(self):
        # f(x) = 3x√(x² + 1) en [1, 2] con n=4
        f = lambda x: 3 * x * math.sqrt(x**2 + 1)
        resultado = trapecio(f, 1, 2, 4)
        self.assertAlmostEqual(resultado, 8.381664, places=3)

    def test2(self):
        # f(x) = sin(x) en [0, π] con n=4
        f = lambda x: math.sin(x)
        resultado = trapecio(f, 0, math.pi, 4)
        self.assertAlmostEqual(resultado, 1.8961, places=3)

if __name__ == "__main__":
    unittest.main()