from typing import List
import unittest


class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x + 1
        ans = -1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid * mid <= x:
                ans = mid
                lo = mid + 1
            else:
                hi = mid
        return ans



class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            (0, 0),
            (1, 1),
            (2, 1),
            (4, 2),
            (8, 2),
            (15, 3),
            (2147395599, 46339),
            (2147483647, 46340),
        ]
        self.s = Solution()

    def test_solution(self):
        for x, answer in self.test_case:
            ans = self.s.mySqrt(x)
            self.assertEqual(answer,ans , (x, answer))


if __name__ == '__main__':
    unittest.main()
