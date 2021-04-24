from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l, r = 0, len(height) - 1

        while l < r:
            if height[l] < height[r]:
                area = height[l] * (r - l)
                l += 1
            else:
                area = height[r] * (r - l)
                r -= 1
            ans = max(ans , area)
        return ans


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.input = [
            [1, 8, 6, 2, 5, 4, 8, 3, 7],
            [1, 1],
            [4, 3, 2, 1, 4]
        ]
        self.answer = [49, 1, 16]
        self.s = Solution()

    def test_solution(self):
        for i, item in enumerate(self.input):
            ans = self.s.maxArea(item)
            self.assertEqual(ans , self.answer[i],ans )


if __name__ == '__main__':
    unittest.main()
