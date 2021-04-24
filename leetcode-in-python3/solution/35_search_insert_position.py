from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target: # 绝对小于，右半边
                lo = mid + 1
            else:
                hi = mid
        return hi


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.input = [
            ([1,3,4,6], 7),
            ([4,5,5,5,], 5),
        ]
        self.answer = [
            4,
            1,
        ]
        self.s = Solution()

    def test_solution(self):
        for i, (item, target) in enumerate(self.input):
            ans = self.s.searchInsert(item, target)
            self.assertEqual(ans , self.answer[i],ans )


if __name__ == '__main__':
    unittest.main()
