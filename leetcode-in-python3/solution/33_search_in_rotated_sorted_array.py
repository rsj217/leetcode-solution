from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi-1]:
                    lo = mid + 1
                else:
                    hi = mid
        return -1

import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([4, 5, 6, 7, 0, 1, 2], 0, 4),
            ([4, 5, 6, 7, 0, 1, 2], 3, -1),
            ([1], 0, -1),
            ([5], 1, -1),
            ([5], 5, 0),
            ([4, 5], 3, -1),
            ([4, 5], 4, 0),
            ([4, 5], 5, 1),
            ([4, 5], 6, -1),
            ([5, 4], 3, -1),
            ([5, 4], 4, 1),
            ([5, 4], 5, 0),
            ([6, 7, 1, 2, 3], 7, 1),
            ([5, 6, 2, 3], 2, 2),
            ([6, 7, 0, 2, 3], 2, 3),
            ([6, 7, 0, 2, 3], 6, 0),
            ([6, 7, 0, 2, 3], 6, 0),
        ];
        self.s = Solution()

    def test_solution(self):
        for item, target, answer in self.test_case:
            ans = self.s.search(item, target)
            self.assertEqual(ans , answer,ans )


if __name__ == '__main__':
    unittest.main()
