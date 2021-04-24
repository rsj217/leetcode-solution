import random
from typing import List
from datastruct.treenode import TreeNode
import unittest


class Solution:
    def flatten(self, root: TreeNode) -> None:
        num = random.randint(0, 1)
        num = 1
        d = {
            0: self.flatten_by_dfs_iter,
            1: self.flatten_by_dfs_recursion,
        }
        return d[num](root)

    def flatten_by_dfs_recursion(self, node: TreeNode):
        def merge_left_right(left: TreeNode, right: TreeNode) -> TreeNode:
            if left is None:
                return right
            if right is None:
                return left
            parent = None
            node = left
            while node is not None:
                parent = node
                node = node.right
            parent.right = right
            return left

        if node is None:
            return

        left = node.left
        right = node.right
        self.flatten_by_dfs_recursion(left)
        self.flatten_by_dfs_recursion(right)
        node.right = merge_left_right(left, right)
        node.left = None

    def flatten_by_dfs_iter(self, node: TreeNode):
        if node is None:
            return
        parent = None
        stack = [node]
        while len(stack) > 0:
            node = stack.pop()
            if parent is not None:
                parent.right = node
                parent.left = None
            parent = node
            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:
                stack.append(node.left)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 5, 3, 4, None, 6], [1, None, 2, None, 3, None, 4, None, 5, None, 6]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            answer = TreeNode.create(answer)
            ans = self.s.flatten(root)
            # TODO

if __name__ == '__main__':
    unittest.main()
