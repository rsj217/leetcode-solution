import unittest
import helper


def merge_left_right(nums, lo, mid, hi):
    tmp_nums = [0 for i in range(lo, hi)]
    lsize, rsize = mid - lo, hi - lo
    l, r = lo - lo, mid - lo
    for i in range(hi - lo):
        if l < lsize and r < rsize:
            if tmp_nums[l] <= tmp_nums[r]:
                nums[i] = tmp_nums[l]
                l += 1
            else:
                nums[i] = tmp_nums[r]
                r += 1
        else:
            if l < lsize:
                nums[i] = tmp_nums[l]
                l += 1
            else:  # r < rsize:
                nums[i] = tmp_nums[r]
                r += 1


def merge_sort(nums):
    def dfs(nums, lo, hi):
        if hi - lo <= 1:
            return
        mid = lo + (hi - lo) // 2
        dfs(nums, lo, mid)
        dfs(nums, mid, hi)
        merge_left_right(nums, lo, mid, hi)

    dfs(nums, 0, len(nums))


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
            merge_sort(nums)
            self.assertTrue(helper.is_sorted(nums))


if __name__ == '__main__':
    unittest.main()
