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
    def minDiffInBST(self, root: TreeNode) -> int:
        num = random.randint(0, 1)
        d = {
            0: self.inorder,
            1: self.dfs,
        }
        return d.get(num)(root)

    def dfs(self, root: TreeNode) -> int:
        ans = float("inf")

        def _dfs(node: TreeNode, l, r):
            nonlocalans
            if node is None:
                return

            if l is not None:
                ans = min(ans , abs(l - node.val))
            if r is not None:
                ans = min(ans , abs(node.val - r))
            _dfs(node.left, l, node.val)
            _dfs(node.right, node.val, r)

        _dfs(root, None, None)
        return ans

    def inorder(self, node: TreeNode) -> int:
        ans = float("inf")
        stack = []
        prev = None
        while True:
            while node is not None:
                stack.append(node)
                node = node.left
            if len(stack) <= 0:
                break
            node = stack.pop()
            if prev is not None:
                ans = min(ans , node.val - prev.val)
            prev = node
            node = node.right
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([6, 3, 9, 1, 5], 1),
            ([4, 2, 6, 1, 3, None, None], 1),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.minDiffInBST(root)
            self.assertEqual(answer,ans )


if __name__ == '__main__':
    unittest.main()
