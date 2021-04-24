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
    def increasingBST(self, root: TreeNode) -> TreeNode:
        num = random.randint(0, 1)
        d = {
            0: self.inorder,
            1: self.dfs,
        }
        return d.get(num)(root)

    def dfs(self, node: TreeNode) -> TreeNode:
        if node is None:
            return
        left = self.increasingBST(node.left)
        right = self.increasingBST(node.right)

        node.right = right
        node.left = None
        if left is None:
            return node
        node = left
        prev = None
        while node is not None:
            prev = node
            node = node.right

        prev.right = node
        return left

    def inorder(self, node: TreeNode) -> TreeNode:
        if node is None:
            return

        head = TreeNode(val=0)
        prev = head
        node = node
        stack = []
        while True:
            while node is not None:
                stack.append(node)
                node = node.left
            if len(stack) <= 0:
                break

            node = stack.pop()
            node.left = None
            prev.right = node
            prev = node
            node = node.right
        return head.right


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([2, 1, 4, None, None, 3], 1),  # TODO
            ([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9], 1)
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.increasingBST(root)
            # self.assertEqual(answer,ans )
            while ans is not None:
                print(ans .val)
                print(ans .left)
                ans =ans .right


if __name__ == '__main__':
    unittest.main()
