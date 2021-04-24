from typing import List
import random


def is_sorted(nums: List[int]) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


def random_nums(size, l, r) -> List[int]:
    return [random.randint(l, r) for i in range(size)]
