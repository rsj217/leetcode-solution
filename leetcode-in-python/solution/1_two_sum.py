from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t = dict()
        for i in range(len(nums)):
            index = t.get(target - nums[i])
            if index is not None:
                return [index, i]
            t[nums[i]] = i
        return []
