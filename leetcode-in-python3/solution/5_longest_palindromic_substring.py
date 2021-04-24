
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for index, _ in enumerate(s):
            s1 = self._longestPalindrome(s, index, index)
            s2 = self._longestPalindrome(s, index, index + 1)
            ss = s2 if len(s1) <= len(s2) else s1
            if len(ans ) < len(ss):
                ans = ss
        return ans

    def _longestPalindrome(self, s: str, l: int, r: int):
        while 0 <= l and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.input = ["babad", "cbbd", "a", "", "ab", "aa"]
        self.answer = ["bab", "bb", "a", "", "a", "aa"]
        self.s = Solution()

    def test_solution(self):
        for i, s in enumerate(self.input):
            ans = self.s.longestPalindrome(s)
            self.assertEqual(ans , self.answer[i],ans )


if __name__ == '__main__':
    unittest.main()
