from typing import List
import unittest


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i, _ in enumerate(prices[1:],1):
            if prices[i-1] < prices[i]:
                ans += prices[i] - prices[i-1]
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([7, 1, 5, 3, 6, 4], 7),
            ([7, 6, 4, 3, 1], 0),
            ([5], 0),
            ([4, 5], 1),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            ans = self.s.maxProfit(nums)
            self.assertEqual(answer,ans , (nums, answer))


if __name__ == '__main__':
    unittest.main()
