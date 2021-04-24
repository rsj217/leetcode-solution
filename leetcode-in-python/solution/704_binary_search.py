from typing import List
import unittest


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:  # 区间至少有一个元素
            mid = lo + (hi - lo) // 2  # 不能使用 (lo + hi) // 2, lo + hi 有可能异出，在rust版本中就不能编译通过

            if target == nums[mid]:  # mid命中，直接返回
                return mid

            elif target < nums[mid]:  # target 在左半边
                hi = mid  # 将 hi 移动到 mid，即左半区间 [lo, mid) 不包括 mid

            else:  # nums[mid] < target:     # target 在右半边
                lo = mid + 1  # 将 lo 移动到 mid + 1，即右半区间 [mid+1, hi)
        return -1


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([-1, 0, 3, 5, 9, 12], 9, 4),
            ([-1, 0, 3, 5, 9, 12], 2, -1),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, target, answer in self.test_case:
            ans = self.s.search(nums, target)
            self.assertEqual(answer,ans , (nums, answer))


if __name__ == '__main__':
    unittest.main()
