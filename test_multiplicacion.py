import unittest

from multiplicacion import multiplicar

class TestMultiplicar(unittest.TestCase):
     def test_multiplicar(self):
       
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(1, 1), 1)
        self.assertEqual(multiplicar(40, 7), 280)
        self.assertEqual(multiplicar(4, 0), 0)
        self.assertEqual(multiplicar(5, -2), -10)
if __name__ == '__main__':
 unittest.main()
