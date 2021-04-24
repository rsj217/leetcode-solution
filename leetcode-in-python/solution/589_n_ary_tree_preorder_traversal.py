from typing import List


class Solution:
    def guessNumber(self, n: int) -> int:
        pass


import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            (10, 6),
            (1, 1),
            (2, 1),
            (2, 2),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            ans = self.s.guessNumber(nums)
            self.assertEqual(answer,ans , (nums, answer))


if __name__ == '__main__':
    unittest.main()
