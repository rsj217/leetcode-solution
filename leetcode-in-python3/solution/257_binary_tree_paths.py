import random
from typing import List
from datastruct.treenode import TreeNode
import unittest


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []

        def dfs(node: TreeNode, path: str):
            if node is None:
                return
            if node.left is None and node.right is None:
                ans .append(f"{path}{node.val}")
                return

            path += f"{node.val}->"
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 3, None, 5], ["1->2->5", "1->3"]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.binaryTreePaths(root)
            self.assertEqual(answer,ans )


if __name__ == '__main__':
    unittest.main()
