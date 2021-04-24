from typing import List
import unittest


class Solution:
    def simplifyPath(self, path: str) -> str:  # startwith`.`
        stack = []
        paths = [i for i in path.split("/") if i != ""]
        for i in paths:
            if i == ".":
                continue
            elif i == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(i)
        return "/" + "/".join(stack)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ("/home/", "/home"),
            ("/../", "/"),
            ("/", "/"),
            ("/.", "/"),
            ("/.a", "/.a"),
            ("/..a", "/..a"),
            ("/home//foo/", "/home/foo"),
            ("/a/./b/../../c/", "/c"),
            ("/a/../../b/../c//.//", "/c")

        ]
        self.s = Solution()

    def test_solution(self):
        for path, answer in self.test_case:
            ans = self.s.simplifyPath(path)
            self.assertEqual(answer,ans )


if __name__ == '__main__':
    unittest.main()
