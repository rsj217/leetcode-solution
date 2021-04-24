from typing import List
from datastruct.treenode import TreeNode
import unittest
import random


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if random.randint(0, 1):
            return list(self._inorderTraversal(root))
        return self._inorderTraversal_iter(root)

    def _inorderTraversal(self, node: TreeNode) -> List[int]:
        if node is None:
            return
        yield from self._inorderTraversal(node.left)
        yield node.val
        yield from self._inorderTraversal(node.right)

    def _inorderTraversal_iter(self, root: TreeNode) -> List[int]:
        ans = []
        if root is None:
            return ans
        stack = []
        node = root
        while True:
            while node is not None:
                stack.append(node)
                node = node.left
            if len(stack) <= 0:
                break
            node = stack.pop()
            ans .append(node.val)
            node = node.right
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([], []),
            ([], []),
        ]
        self.s = Solution()

    def test_solution(self):
        pass


if __name__ == '__main__':
    unittest.main()
