"""
Created on 27.12.2013

@author: uhs374h
"""
import unittest
from bruch.Bruch import *


class TestAllgemein(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = self.b
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def testFloat(self):
        b = Bruch(3, 4)
        assert(float(b.value) == 0.75)

    def testInt(self):
        b = Bruch(5, 4)
        assert(int(b.value) == 1)

    def testComplex(self):
        b = Bruch(3, 4)
        assert(complex(b.value) == 0.75)

    def testInvert(self):
        z, n = 5, 4
        b = Bruch(z, n)
        assert(~b != int(Bruch(n, z).value))

    def testcreateBruchZeroError(self):
        self.assertRaises(ZeroDivisionError, Bruch, 3, 0)

    def testcreateBruchWrongTypeNenner(self):
        self.assertRaises(TypeError, Bruch, 3, 1.1)

    def testcreateBruchWrongTypeZaehler(self):
        self.assertRaises(TypeError, Bruch, 2.0)

    def testInteger(self):
        self.b2 = Bruch(3, 1)
        assert(int(self.b2.value) == 3)

    def testPow(self):
        h = 4
        assert(self.b2.value ** h == Bruch(self.b2.zaehler ** h, self.b2.nenner ** h).value)

    def testPowError1(self):
        self.assertRaises(TypeError, self.b2.__pow__, 2.0)

    def testPowError2(self):
        self.assertRaises(TypeError, self.b2.__pow__, "other")

    def test_makeBruchTypeError(self):
        self.assertRaises(TypeError, Bruch._Bruch__makeBruch, "other")

    def test_makeBruchInt(self):
        b4 = Bruch(-3, 2)
        value = 3
        b4._Bruch__makeBruch(value)
        assert(b4.zaehler == value)

    def testAbs(self):
        b4 = Bruch(-3, 2)
        assert(abs(b4.value) == Bruch(3, 2).value)

    def testNeg(self):
        b4 = Bruch(-3, 2)
        assert(-b4.value == Bruch(3, 2).value)

    # test of references
    def testRef(self):
        assert(AssertionError, self.b != self.b2)

    def testRef2(self):
        b4 = self.b
        assert(self.b is b4)


class TestVergleich(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = self.b
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def testEqual(self):
        assert(self.b.value == self.b2.value)

    def testNotEqual(self):
        assert(self.b.value != self.b3.value)

    def testGE(self):
        assert(self.b.value >= self.b2.value)

    def testLE(self):
        assert(self.b.value <= self.b2.value)

    def testLT(self):
        assert(self.b.value < self.b3.value)

    def testGT(self):
        assert(self.b3.value > self.b2.value)


class TestString(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = self.b
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def teststr(self):
        str1 = str(3/2)
        assert(str(self.b.value) == str1)

    def teststr2(self):
        b2 = Bruch(-3, -2)
        str1 = str(3/2)
        assert(str(b2.value) == str1)


class TestAddition(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = self.b
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def testplus(self):
        self.b = self.b.value + Bruch(4, 5).value
        assert(float(self.b) == 2.3)

    def testplus2(self):
        self.b = self.b.value + self.b3.value
        assert(float(self.b) == 3.5)

    def testplus3(self):
        self.b2 = self.b.value + 3
        assert(float(self.b2) == 4.5)

    def testradd(self):
        self.b2 = 3 + Bruch(3, 2).value
        assert(float(self.b2) == 4.5)

    def testiAdd(self):
        self.b += 1
        assert(self.b == Bruch(5, 2).value)

    def testiAdd2(self):
        self.b += Bruch(1).value
        assert(self.b == Bruch(5, 2).value)

    def testaddError(self):
        self.assertRaises(TypeError, self.b2.__add__, 2.0)

    def testiAddError(self):
        self.assertRaises(TypeError, self.b.__iadd__, "other")


class TestSubtraktion(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = self.b
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def testminus(self):
        self.b = self.b.value - Bruch(4, 5).value
        assert(float(self.b) == 0.7)

    def testminus2(self):
        self.b = self.b.value - self.b3.value
        assert(float(self.b) == -0.5)

    def testminus3(self):
        self.b2 = self.b.value - Bruch(1).value
        assert(float(self.b2) == 0.5)

    def testiSubError(self):
        self.assertRaises(TypeError, self.b.__isub__, "other")

    def testrsubError(self):
        """TypeError!!!

        self.b2=2.0-self.b2
        """
        self.assertRaises(TypeError, self.b2.__rsub__, 2.0)

    def testiSub(self):
        self.b -= 2
        assert(self.b == Bruch(-1, 2).value)

    def testiSub2(self):
        self.b -= Bruch(2).value
        assert(self.b == Bruch(-1, 2).value)

    def testrsub(self):
        self.b2 = 3 - Bruch(3, 2).value
        assert(float(self.b2) == 1.5)


class TestMultiplikation(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = self.b
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def testmal(self):
        self.b = self.b.value * Bruch(4).value
        assert(float(self.b) == 6)

    def testmal2(self):
        self.b = self.b.value * self.b2.value
        assert(float(self.b) == 2.25)

    def testmal3(self):
        self.b2 = self.b.value * 2
        assert(float(self.b2) == 3)

    def testiMulError(self):
        self.assertRaises(TypeError, self.b.__imul__, "other")

    def testiMul(self):
        self.b *= 2
        assert(self.b == 3)

    def testiMul2(self):
        self.b *= Bruch(2).value
        assert(self.b == 3)

    def testrmal(self):
        self.b2 = 2 * Bruch(3, 2).value
        assert(float(self.b2) == 3)

    def testmulError(self):
        self.assertRaises(TypeError, self.b2.__mul__, 2.0)


class TestDivision(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = self.b
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def testdiv(self):
        self.b = self.b.value / Bruch(4).value
        assert(float(self.b) == 0.375)

    def testdiv2(self):
        self.b = self.b.value / self.b3.value
        assert(float(self.b) == 0.75)

    def testdiv3(self):
        self.b2 = self.b.value / 2
        assert(float(self.b2) == 0.75)

    def testrdivError(self):
        self.assertRaises(TypeError, self.b2.__rtruediv__, 3.0)

    def testrdiv(self):
        self.b2 = 2 / Bruch(2).value
        assert(float(self.b2) == 1)

    def testdivZeroError(self):
        self.assertRaises(ZeroDivisionError, self.b2.__truediv__, 0)

    def testdivTypeError(self):
        self.assertRaises(TypeError, self.b2.__truediv__, 3.1)

    def testdivZeroError2(self):
        self.assertRaises(ZeroDivisionError, self.b2.__truediv__, Bruch(0, 3).value)

    def testrdivZeroError(self):
        bneu = Bruch(0, 3)
        self.assertRaises(ZeroDivisionError, bneu.__rtruediv__, 0)

    def testiDiv(self):
        self.b /= 2
        assert(self.b == Bruch(3, 4).value)

    def testiDiv2(self):
        self.b /= Bruch(2).value
        assert(self.b == Bruch(3, 4).value)

    def testiDivError(self):
        self.assertRaises(TypeError, self.b.__itruediv__, "other")


class TestIteration(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = self.b
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def testTuple(self):
        z, n = Bruch(3, 4).__repr__()
        assert(z == 3 and n == 4)

    def testTuple2(self):
        z, n = self.b.__repr__()
        self.assertEqual(Bruch(z, n).value, self.b.value)

    def testTuple3_Error(self):
        b3 = self.b2.__repr__()
        self.assertRaises(IndexError, self.tryIndex, b3, 3)

    @staticmethod
    def tryIndex(obj, index):
        return obj[index]

if __name__ == "__main__":
    unittest.main()
