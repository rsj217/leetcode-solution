import random
from typing import List
from datastruct.treenode import TreeNode
import unittest


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        num = random.randint(0, 1)
        num = 1
        d = {
            0: self.invert_tree_by_dfs,
            1: self.invert_tree_by_bfs,
        }
        return d[num](root)

    def invert_tree_by_dfs(self, node: TreeNode) -> TreeNode:
        if node is None:
            return

        left = self.invert_tree_by_dfs(node.left)
        right = self.invert_tree_by_dfs(node.right)
        node.left = right
        node.right = left
        return node

    def invert_tree_by_bfs(self, node: TreeNode) -> TreeNode:
        if node is None:
            return
        root = node
        queue = [node]

        while len(queue) > 0:
            node = queue.pop(0)
            node.right, node.left = node.left, node.right
            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)
        return root


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
            ([], None),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            answer = TreeNode.create(answer)
            ans = self.s.invertTree(root)
            # self.asertEqual(answer.to_list(),ans .to_list) # TODO


if __name__ == '__main__':
    unittest.main()
