import unittest
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, i, r = 0, 0, len(nums) - 1
        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:  # nums[i] == 2
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
            ([2, 0, 1], [0, 1, 2]),
            ([0, 1, 0], [0, 0, 1]),
            ([0], [0]),
            ([1], [1]),
            ([2], [2]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            self.s.sortColors(nums)
            self.assertEqual(nums, answer)


if __name__ == '__main__':
    unittest.main()
