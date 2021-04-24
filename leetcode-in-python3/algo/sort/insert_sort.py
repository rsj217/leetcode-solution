from typing import List
import unittest
import helper


def insert_sort(nums: List[int]):
    size = len(nums)
    for i in range(size):
        j = i
        num_i = nums[i]
        while 0 < j and num_i < nums[j - 1]:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = num_i


class TestMain(unittest.TestCase):

    def setUp(self) -> None:
        self.test_case = [
            [],
            [0, 0, 0],
            [10, 3, 1, 1],
            helper.random_nums(100, 0, 100)
        ]

    def test_solution(self):
        for nums in self.test_case:
            insert_sort(nums)
            self.assertTrue(helper.is_sorted(nums))


if __name__ == '__main__':
    unittest.main()
