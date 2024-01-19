import unittest

from resta import restar

class TestRestar(unittest.TestCase):
     def test_restar(self):
       
        self.assertEqual(restar(3, 2), 1)
        self.assertEqual(restar(1, -1), 2)
        self.assertEqual(restar(40, 7), 33)
        self.assertEqual(restar(8, 0), 8)
if __name__ == '__main__':
 unittest.main()
