import random
from typing import List
from datastruct.treenode import TreeNode
import unittest
from collections import deque


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        num = random.randint(0, 1)
        d = {
            0: self.bfs,
            1: self.dfs,
        }
        return d.get(num)(root)

    def bfs(self, node: TreeNode) -> List[int]:
        if node is None:
            return []
        ans = []
        queue = deque()
        queue.append(node)
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                if i == size - 1:
                    ans .append(node.val)
        return ans

    def dfs(self, node: TreeNode) -> List[int]:
        ans = []
        visit = {}

        def _dfs(node: TreeNode, level):
            if node is None:
                return
            if not visit.get(level, False):
                ans .append(node.val)
                visit[level] = True
            _dfs(node.right, level + 1)
            _dfs(node.left, level + 1)

        _dfs(node, 0)
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 3, None, 5, None, 4, 6], [1, 3, 4, 6])
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.rightSideView(root)
            self.assertEqual(answer,ans )


if __name__ == '__main__':
    unittest.main()
