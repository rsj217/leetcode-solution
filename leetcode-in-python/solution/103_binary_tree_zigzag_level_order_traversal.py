from typing import List
from datastruct.treenode import TreeNode
from collections import deque
import random
import unittest


class Solution:

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        return self.bfs(root)

    def bfs(self, node: TreeNode) -> List[List[int]]:
        if node is None:
            return []
        ans = []
        queue = deque()
        queue.append(node)
        l2r = True
        while len(queue) > 0:
            size = len(queue)
            level = deque()
            for _ in range(size):
                node = queue.popleft()
                if l2r:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)
            l2r = not l2r
            ans.append(list(level))
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([3, 9, 20, None, None, 15, 7], [
                [3],
                [20, 9],
                [15, 7],
            ]),
            ([1, 2, 3, 4, 5], [
                [1],
                [3, 2],
                [4, 5]
            ]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.zigzagLevelOrder(root)
            print(ans)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
