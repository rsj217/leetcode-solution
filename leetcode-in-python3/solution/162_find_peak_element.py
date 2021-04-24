from typing import List
import unittest


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)
        while 1 < hi - lo:  # 还剩一个元素
            mid = lo + (hi - lo) // 2
            if nums[mid - 1] > nums[mid]:
                hi = mid
            else:  # nums[mid] < nums[mid+1] or nums[mid] > nums[mid+1]
                lo = mid
        return lo


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 1, 3, 5, 6, 4], [1, 5]),
            ([1, 2, 3, 1], [2]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            ans = self.s.findPeakElement(nums)
            print(answer)
            self.assertIn(ans , answer)


if __name__ == '__main__':
    unittest.main()
