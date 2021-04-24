import random
from typing import List
from datastruct.treenode import TreeNode
import unittest


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return

        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root
        if left is None:
            return right
        if right is None:
            return left


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),
            ([1, 2], 1, 2, 1),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, p, q, answer in self.test_case:
            root = TreeNode.create(nums)
            p = TreeNode(p)
            q = TreeNode(q)
            ans = self.s.lowestCommonAncestor(root, p, q)
            self.assertEqual(answer,ans .val)


if __name__ == '__main__':
    unittest.main()
