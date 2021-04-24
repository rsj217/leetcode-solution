from typing import List
import unittest


class Solution:

    def digit_letter(self, x: str) -> str:
        return {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }.get(x)

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        return self._letterCombinations(digits)

    def _letterCombinations(self, digits: str) -> List[str]:
        if len(digits) <= 1:
            return [i for i in self.digit_letter(digits[0])]
        head_letters = [i for i in self.digit_letter(digits[0])]
        tail_letters = self._letterCombinations(digits[1:])
        return [i + j for i in head_letters for j in tail_letters]


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
            ("", [])
        ]
        self.s = Solution()

    def test_solution(self):
        for digits, answer in self.test_case:
            ans = self.s.letterCombinations(digits)
            self.assertEqual(answer,ans )


if __name__ == '__main__':
    unittest.main()
