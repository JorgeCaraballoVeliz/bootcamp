import unittest

from division import dividir

class TestDividir(unittest.TestCase):
     def test_dividir(self):
       
        self.assertEqual(dividir(4, 2), 2)
        self.assertEqual(dividir(1, 1), 1)
        self.assertEqual(dividir(40, 5), 8)
if __name__ == '__main__':
 unittest.main()
