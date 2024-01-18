import unittest

from resta import restar

class TestRestar(unittest.TestCase):
     def test_restar(self):
       
        self.assertEqual(restar(3, 2), 1)
        self.assertEqual(restar(1, 1), 0)
        self.assertEqual(restar(40, 7), 33)
if __name__ == '__main__':
 unittest.main()
