from collections import deque
from datastruct.treenode import TreeNode
import unittest
import random


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        num = random.randint(0, 1)
        d = {
            0: self.inorder,
            1: self.dfs,
        }
        return d.get(num)(root)

    def dfs(self, root: TreeNode) -> TreeNode:
        def dfs_(node: TreeNode, sum_: int) -> int:
            if node is None:
                return sum_
            sum_ = dfs_(root.right, sum_)
            sum_ += node.val
            node.val = sum_
            return dfs_(root.left, sum_)

        dfs_(root, 0)
        return root

    def inorder(self, root: TreeNode) -> TreeNode:
        if root is None:
            return

        node = root
        sum_ = 0
        stack = []
        while True:
            while node is not None:
                stack.append(node)
                node = node.right
            if len(stack) <= 0:
                break

            node = stack.pop()
            sum_ += node.val
            node.val = sum_
            node = node.left
        return root


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8], 15),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.bstToGst(root) # TODO
            # self.assertEqual(answer,ans , (nums, answer))


if __name__ == '__main__':
    unittest.main()
