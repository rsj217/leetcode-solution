import random
from typing import List
from datastruct.treenode import TreeNode
import unittest
from collections import deque


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        num = random.randint(0, 2)
        nums = 0
        d = {
            0: self.bfs,
            1: self.dfs,
            2: self.preorder,
        }
        return d.get(num)(root)

    def preorder(self, node: TreeNode) -> int:
        if node is None:
            return 0

        ans = node.val
        max_level = -1

        stack = [(node, 0)]
        while len(stack) > 0:
            node, level = stack.pop()
            if node.left is None and node.right is None:
                if max_level < level:
                    ans = node.val
                    max_level = level

            if node.right is not None:
                stack.append((node.right, level + 1))

            if node.left is not None:
                stack.append((node.left, level + 1))

        return ans

    def bfs(self, node: TreeNode) -> int:
        if node is None:
            return 0
        ans = 0
        queue = deque()
        queue.append(node)
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == 0:
                    ans = node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return ans

    def dfs(self, node: TreeNode) -> int:
        ans = 0
        max_level = -1

        def dfs(node: TreeNode, level: int):
            nonlocal max_level, ans
            if node is None:
                return

            if node.left is None and node.right is None:
                if max_level < level:
                    max_level = level
                    ans = node.val
                    return

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(node, 0)
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1], 1),
            ([2, 1, 3], 1),
            ([1, 2, 3, 4, 5, 6, None, None, 7], 7),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.findBottomLeftValue(root)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
