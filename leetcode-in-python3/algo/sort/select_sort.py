from typing import List
import unittest


def select_sort(nums: List[int]):
    size = len(nums)
    for i in range(size):
        min_i = i
        for j in range(i, size):
            if nums[j] < nums[min_i]:
                min_i = j
        nums[i], nums[min_i] = nums[min_i], nums[i]


class TestMain(unittest.TestCase):

    def setUp(self) -> None:
        self.test_case = [
            [],
            [0, 0, 0],
            [0, 3, 1, 1],
        ]

    def test_solution(self):
        for nums in self.test_case:
            n = nums[:]
            select_sort(nums)
            print(nums)


if __name__ == '__main__':
    unittest.main()
