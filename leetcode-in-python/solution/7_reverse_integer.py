class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        # [-2147483648, 2147483647]
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31

        while x != 0:
            if x > 0:
                pop = x % 10
                x = x // 10
            else:
                pop = x % - 10
                x = -(x // -10)

            if ans > MAX_INT / 10 or (ans == MAX_INT and pop > 7):  # 2147483647 = 2147483640 + 7
                return 0
            if ans < MIN_INT / 10 or (ans == MIN_INT and pop < -8):  # -2147483648 = -2147483640 +(-8)
                return 0
            ans = ans * 10 + pop
        return ans

import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.input = [123, 0, -123, 2147483647, 1463847412, 1463847413, 1534236469]
        self.answer = [321, 0, -321, 0, 2147483641, 0, 0]
        self.s = Solution()

    def test_solution(self):
        for i, item in enumerate(self.input):
            ans = self.s.reverse(item)
            self.assertEqual(ans , self.answer[i],ans )


if __name__ == '__main__':
    unittest.main()
