from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == nums[r]:
                r -= 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]


import unittest
import solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([3, 4, 5, 1, 2], 1),
            ([4, 5, 6, 7, 0, 1, 2], 0),
            ([4, 5, 6, 7, 0, 1, 2], 0),
            ([5], 5),
            ([4, 5], 4),
            ([5, 4], 4),
            ([6, 7, 1, 2, 3], 1),
            ([5, 6, 2, 3], 2),
            ([6, 7, 0, 2, 3], 0),
            ([4, 0, 3], 0),
            ([4, 3], 3),
            ([2,2,2,0,1], 0),
        ]
        self.s = solution.Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            ans = self.s.findMin(nums)
            self.assertEqual(answer,ans , (nums, answer))


if __name__ == '__main__':
    unittest.main()
