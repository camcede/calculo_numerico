import math
import unittest

from src.biseccion import biseccion

class TestBiseccion(unittest.TestCase):

    def test1(self):
        # f(x) = e^{-x} - ln(x)
        f = lambda x: math.exp(-x) - math.log(x)
        a, b = 1, 1.5
        er = 0.01
        n = 100
        raiz_esperada = 1.3046875
        resultado = biseccion(f, a, b, er, n)
        self.assertAlmostEqual(resultado[0], raiz_esperada, delta=0.02)
        self.assertLess(resultado[1], er)

    def test2(self):
        # f(x) = x^2 - 4
        f = lambda x: x**2 - 4
        a, b = 0, 3
        er = 0.01
        n = 100
        raiz_esperada = 2.00390625
        resultado = biseccion(f, a, b, er, n)
        self.assertAlmostEqual(resultado[0], raiz_esperada, delta=0.02)
        self.assertLess(resultado[1], er)

if __name__ == '__main__':
    unittest.main()
