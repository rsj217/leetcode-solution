from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 0:
            return ""

        min_str = strs[0]
        for s in strs:
            if len(s) < len(min_str):
                min_str = s

        hi = 0
        for i, item in enumerate(min_str):
            for w in strs:
                if item != w[i]:
                    return min_str[0:i]
            hi += 1
        return min_str[0:hi]



import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.input = [
            ["flower", "flow", "flight"],
            ["dog", "racecar", "car"],
            ["", "", ""],
            ["", "qwe"],
            [],
            [""],
            ["a"],
            ["abc", "abc"],

        ]
        self.answer = [
            "fl",
            "",
            "",
            "",
            "",
            "",
            "a",
            "abc",
        ]
        self.s = Solution()

    def test_solution(self):
        for i, item in enumerate(self.input):
            ans = self.s.longestCommonPrefix(item)
            self.assertEqual(ans , self.answer[i],ans )


if __name__ == '__main__':
    unittest.main()
