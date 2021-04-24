from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return True
            elif nums[lo] == nums[mid]:
                lo += 1
            elif nums[lo] < nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi-1]:
                    lo = mid + 1
                else:
                    hi = mid
        return False


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([2, 5, 6, 0, 0, 1, 2], 0, True),
            ([2, 5, 6, 0, 0, 1, 2], 3, False),
            ([1, 0, 1, 1, 1], 0, True),
            ([1, 1, 1, 2, 1], 2, True),
            ([5, 1, 3], 3, True)
        ];
        self.s = Solution()

    def test_solution(self):
        for item, target, answer in self.test_case:
            ans = self.s.search(item, target)
            self.assertEqual(ans , answer,ans )


if __name__ == '__main__':
    unittest.main()
