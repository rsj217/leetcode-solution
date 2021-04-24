from typing import List
import unittest


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        assert len(prices) != 0, "prices empty"
        ans = 0
        min_buy_price = prices[0]
        for cur_price in prices:
            if min_buy_price < cur_price:
                ans = max(ans , cur_price - min_buy_price)
            else:
                min_buy_price = cur_price
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([7, 1, 5, 3, 6, 4], 5),
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
