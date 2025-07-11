import math
import unittest
from src.riemann import suma_riemann

class TestSumaRiemann(unittest.TestCase):

    def test1(self):
        # f(x) = 3x√(x² + 1) en [1, 2] con n=4
        f = lambda x: 3 * x * math.sqrt(x**2 + 1)
        resultado = suma_riemann(f, 1, 2, 4)
        self.assertAlmostEqual(resultado, 7.23494, places=3)

    def test2(self):
        # f(x) = x^2 en [0, 1] con n=4
        f = lambda x: x**2
        resultado = suma_riemann(f, 0, 1, 4)
        self.assertAlmostEqual(resultado, 0.21875, places=3)

if __name__ == "__main__":
    unittest.main()