import random
from typing import List
from datastruct.treenode import TreeNode
import unittest
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.dfs(root)

    def dfs(self, node: TreeNode) -> int:
        ans = 0

        def _dfs(node: TreeNode) -> int:
            nonlocal ans
            if node is None:
                return 0
            left = _dfs(node.left)
            right = _dfs(node.right)
            ans = max(ans, left + right + 1)
            return 1 + max(left, right)

        _dfs(node)
        return ans - 1


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 3, None, None, 5, 6, 7, 8, 9, None, None, None, 0, None, 1], 6),
            ([1, 2, 3, None, 4, 5, 6], 4),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.diameterOfBinaryTree(root)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
