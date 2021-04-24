from datastruct.treenode import TreeNode
from collections import deque
import random
import unittest


class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        num = random.randint(0, 1)
        d = {
            0: self.dfs,
            1: self.postorder,
            2: self.bfs
        }
        return d[num](root)

    def postorder(self, node: TreeNode) -> int:
        if node is None:
            return 0

        ans = 0
        deep = 1

        stack = []
        prev_node = None

        while True:
            while node is not None:
                stack.append((node, deep))
                deep += 1
                node = node.left

            if len(stack) <= 0:
                break

            if stack[-1][0].right != prev_node:
                node = stack[-1][0].right
                prev_node = None
            else:
                prev_node, deep = stack.pop()
                ans = max(ans, deep)
        return ans

    def bfs(self, root: TreeNode) -> int:
        if root is None:
            return 0
        deep = 0
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            deep += 1
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return deep

    def dfs(self, root: TreeNode) -> int:
        def _dfs(node: TreeNode) -> int:
            if node is None:
                return 0
            return 1 + max(_dfs(node.left), _dfs(node.right))
        return _dfs(root)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([3, 9, 20, None, None, 15, 7], 3),
            ([], 0),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.maxDepth(root)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
