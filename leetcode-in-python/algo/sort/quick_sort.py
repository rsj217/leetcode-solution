import unittest
import helper


def partition(nums, lo, hi):
    j = lo
    for i in range(lo, hi):
        if nums[i] <= nums[lo]:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    nums[lo], nums[j - 1] = nums[j - 1], nums[lo]
    return j - 1


def quick_sort(nums):
    def _quick_sort(nums, lo, hi):
        if hi - lo <= 1:
            return
        p = partition(nums, lo, hi)
        _quick_sort(nums, lo, p)
        _quick_sort(nums, p + 1, hi)

    _quick_sort(nums, 0, len(nums))


def quick_3way_sort(nums):
    def dfs(nums, lo, hi):
        if hi - lo <= 1:
            return
        curnum = nums[lo]
        j, i, k = lo, lo, hi - 1
        while i <= k:
            if nums[i] < curnum:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
                i += 1
            elif curnum < nums[i]:
                nums[i], nums[k] = nums[k], nums[i]
                k -= 1
            else:
                i += 1

        dfs(nums, lo, j)
        dfs(nums, k + 1, hi)

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
            # quick_sort(nums)
            quick_3way_sort(nums)
            self.assertTrue(helper.is_sorted(nums))




if __name__ == '__main__':
    unittest.main()
