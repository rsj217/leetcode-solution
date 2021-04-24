class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        r = 0
        # negative number will not reverse
        while n > 0:
           r = r * 10 + n % 10
           n //= 10
        return x == r


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.input = [123, 121, -121, -0, 0, 1221, 12321]
        self.answer = [False, True, False, True, True, True, True]
        self.s = Solution()

    def test_solution(self):
        for i, item in enumerate(self.input):
            ans = self.s.isPalindrome(item)
            self.assertEqual(ans , self.answer[i],ans )


if __name__ == '__main__':
    unittest.main()
