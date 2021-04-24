from datastruct.treenode import TreeNode
import unittest


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self._isSymmetric(root.left, root.right)

    def _isSymmetric(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        return p.val == q.val and self._isSymmetric(p.left, q.right) and self._isSymmetric(p.right, q.left)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 2, 3, 4, 4, 3], True),
            ([1, 2, 2, None, 3, None, 3], False),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.isSymmetric(root)
            self.assertEqual(answer,ans )


if __name__ == '__main__':
    unittest.main()
