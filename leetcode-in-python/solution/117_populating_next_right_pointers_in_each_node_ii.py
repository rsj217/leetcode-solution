import random
from typing import List
from collections import deque
from datastruct.treenode import TreeNode
import unittest


class Node:
    def __init__(self, val: int = 0):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def connect(self, root: Node) -> Node:
        return self.levelorder(root)

    def levelorder(self, root: Node) -> Node:
        if root is None:
            return

        node = root
        dump_head = Node(0)
        prev = dump_head
        while node is not None:
            if node.left is not None:
                prev.next = node.left
                prev = prev.next
            if node.right is not None:
                prev.next = node.right
                prev = prev.next

            node = node.next
            if node is None:
                node = dump_head.next
                dump_head.next = None
                prev = dump_head
        return root

    def bfs(self, root: Node) -> Node:
        if root is None:
            return root

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


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 3, 4, 5, None, 7], []),
            ([0, 2, 4, 1, None, 3, -1, 5, 1, None, 6, None, 8], [])
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.connect(root)
            # TODO


if __name__ == '__main__':
    unittest.main()
