import unittest
from answer import Solution

class SolutionTest(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(321, Solution().reverse(123))
        self.assertEqual(-321, Solution().reverse(-123))
        self.assertEqual(0, Solution().reverse(0))
        self.assertEqual(0, Solution().reverse(1534236469))
        self.assertEqual(2147483647, Solution().reverse(7463847412))
        self.assertEqual(0, Solution().reverse(-2147483648))
        self.assertEqual(0, Solution().reverse(-8463847412))


if __name__ == "__main__":
  unittest.main()