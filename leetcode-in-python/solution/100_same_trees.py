from datastruct.treenode import TreeNode
import unittest


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 3], [1, 2, 3], True),
            ([1, 2], [1, None, 2], False),
            ([1, 2, 1], [1, 1, 2], False),
        ]
        self.s = Solution()

    def test_solution(self):
        for pp, qq, answer in self.test_case:
            p = TreeNode.create(pp)
            q = TreeNode.create(qq)
            ans = self.s.isSameTree(p, q)
            self.assertEqual(answer,ans )


if __name__ == '__main__':
    unittest.main()
