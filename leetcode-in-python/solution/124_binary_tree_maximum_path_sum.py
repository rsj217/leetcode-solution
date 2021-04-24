import random
from datastruct.treenode import TreeNode
import unittest


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return self.dfs(root)

    def dfs(self, node: TreeNode) -> int:
        ans = -1000

        def _dfs(node: TreeNode) -> int:
            nonlocal ans
            if node is None:
                return -1000
            left = _dfs(node.left)
            right = _dfs(node.right)
            left = max(0, left)
            right = max(0, right)

            ans = max(ans, node.val + left + right)
            return node.val + max(left, right)

        _dfs(node)
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 3], 6),
            ([-10, 9, 20, None, None, 15, 7], 42),
            ([1, 2, 3, 4, None, 5, 6], 16),
            ([1, 2, 3, 1, 3, 5, 6, None, None, None, None, 7, 8, 9], 31),
            ([-3], -3),
            ([-1, -2, -3], -1),
            ([-100, -1, -2], -1),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.maxPathSum(root)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
