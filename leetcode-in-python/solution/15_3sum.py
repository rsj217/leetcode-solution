from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                d = nums[i] + nums[l] + nums[r]
                if d == 0:
                    ans .append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r - 1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
                elif d < 0:
                    l += 1
                else:
                    r -= 1
        return ans


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.input = [
            [-1, 0, 1, 2, -1, -4],
            [],
            [0],
            [0, 0],
            [0, 0, 0, 0],
            [-1, -1, 0, 1],
        ]
        self.answer = [
            [[-1, -1, 2], [-1, 0, 1]],
            [],
            [],
            [],
            [[0, 0, 0]],
            [[-1, 0, 1]],
        ]
        self.s = Solution()

    def test_solution(self):
        for i, item in enumerate(self.input):
            ans = self.s.threeSum(item)
            self.assertEqual(ans , self.answer[i],ans )


if __name__ == '__main__':
    unittest.main()
