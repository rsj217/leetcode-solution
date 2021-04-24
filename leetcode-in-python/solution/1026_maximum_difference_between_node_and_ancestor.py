from collections import deque
from typing import List
from datastruct.treenode import TreeNode, print_tree
import unittest
import random


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node: TreeNode, minimum: int, maximum: int):
            nonlocalans
            if node is None:
                return

            ans = max(ans , abs(node.val - minimum))
            ans = max(ans , abs(node.val - maximum))

            minimum = min(minimum, node.val)
            maximum = max(maximum, node.val)

            dfs(node.left, minimum, maximum)
            dfs(node.right, minimum, maximum)

        dfs(root, root.val, root.val)
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13], 7)
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.maxAncestorDiff(root)
            self.assertEqual(answer,ans , (nums, answer))


if __name__ == '__main__':
    unittest.main()
