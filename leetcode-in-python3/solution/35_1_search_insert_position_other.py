from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if target < nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.input = [
            ([1, 3, 4, 6], 2),
            ([1, 3, 4, 6], 7),
            ([4, 5, 5, 5, ], 5),
        ]
        self.answer = [
            1,
            4,
            4,
        ]
        self.s = Solution()

    def test_solution(self):
        for i, (item, target) in enumerate(self.input):
            ans = self.s.searchInsert(item, target)
            self.assertEqual(ans , self.answer[i],ans )


if __name__ == '__main__':
    unittest.main()
