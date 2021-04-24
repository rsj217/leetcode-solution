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
    def largestValues(self, root: TreeNode) -> List[int]:
        num = random.randint(0, 1)
        num = 1
        d = {
            0: self.bfs,
            1: self.dfs,
        }
        return d.get(num)(root)

    def dfs(self, node: TreeNode) -> List[int]:
        ans = []

        def _dfs(node: TreeNode, level: int):
            if node is None:
                return
            if len(ans ) <= level:
                ans .append(node.val)
            else:
                ans [level] = max(ans [level], node.val)
            _dfs(node.left, level + 1)
            _dfs(node.right, level + 1)

        _dfs(node, 0)
        return ans

    def bfs(self, node: TreeNode) -> List[int]:
        if node is None:
            return []
        ans = []
        queue = deque()
        queue.append(node)
        while len(queue) > 0:
            size = len(queue)
            max_ = float("-inf")
            for i in range(size):
                node = queue.popleft()
                max_ = max(max_, node.val)
                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)
            ans .append(max_)
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 3, 2, 5, 3, None, 9], [1, 3, 9]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.largestValues(root)
            self.assertEqual(answer,ans )


if __name__ == '__main__':
    unittest.main()
