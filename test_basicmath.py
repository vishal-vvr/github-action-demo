import unittest, sys
import basicmath as math

class TestBasicMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(math.add(1,2), 3)
        self.assertEqual(math.add(-1,2), 1)

    def test_sub(self):
        self.assertEqual(math.sub(1,2), -1)
        self.assertEqual(math.sub(-1,2), -3)

    def test_mul(self):
        self.assertEqual(math.mul(1,2), 2)
        self.assertEqual(math.mul(-1,2), -2)

    def test_div(self):
        self.assertEqual(math.div(1,2), 0.5)
        self.assertEqual(math.div(-1,2), -0.5)

if __name__ == "__main__":
    unittest.main()
