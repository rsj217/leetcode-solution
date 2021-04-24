from collections import deque
from datastruct.treenode import TreeNode
import unittest
import random


class Solution:
    max_val = 0
    max_level = 0

    def deepestLeavesSum(self, root: TreeNode) -> int:

        num = random.randint(0, 1)
        d = {
            0: self.dfs,
            1: self.bfs,
        }
        return d[num](root)

    def bfs(self, root: TreeNode) -> int:
        if root is None:
            return 0
        max_val = 0
        max_level = 0
        cur_level = 0

        node = root
        queue = deque()
        queue.append(node)
        while len(queue) > 0:
            size = len(queue)
            cur_level += 1
            for i in range(size):
                node = queue.popleft()

                if node.left is None and node.right is None:
                    if max_level < cur_level:
                        max_level = cur_level
                        max_val = node.val
                    elif max_level == cur_level:
                        max_val += node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return max_val

    def dfs(self, root: TreeNode) -> int:
        max_val = 0
        max_level = 0

        def _dfs(node: TreeNode, level: int):
            nonlocal max_val
            nonlocal max_level
            if node is None:
                return

            if node.left is None and node.right is None:
                if max_level < level:
                    max_level = level
                    max_val = node.val
                elif max_level == level:
                    max_val += node.val

            _dfs(node.left, level + 1)
            _dfs(node.right, level + 1)

        _dfs(root, 0)
        return max_val


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8], 15),
            ([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5], 19),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.deepestLeavesSum(root)
            self.assertEqual(answer,ans , (nums, answer))


if __name__ == '__main__':
    unittest.main()
