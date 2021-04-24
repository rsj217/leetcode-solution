import random
from typing import List
from collections import deque
from datastruct.treenode import TreeNode, print_tree
import unittest


class Node:
    def __init__(self, val: int = 0):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def connect(self, root: Node) -> Node:
        return self.dfs(root)

    def bfs(self, root: Node) -> None:
        if root is None:
            return

        node = root
        queue = deque()
        queue.append(node)
        while len(queue) > 0:
            size = len(queue)
            prev = None
            for i in range(size):
                node = queue.popleft()
                if prev is not None:
                    prev.next = node
                prev = node
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return root

    def dfs(self, root: Node) -> Node:
        def _dfs(node: Node):
            if node is None:
                return
            if node.left is not None and node.right is not None:
                node.left.next = node.right
                if node.next is not None:
                    node.right.next = node.next.left
            _dfs(node.left)
            _dfs(node.right)

        _dfs(root)
        return root


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 3, 4, 5, 6, 7], []),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            print(print_tree(root))
            ans = self.s.connect(root)
            # TODO


if __name__ == '__main__':
    unittest.main()
