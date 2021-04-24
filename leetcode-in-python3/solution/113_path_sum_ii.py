import random
from typing import List
from datastruct.treenode import TreeNode
import unittest


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        num = random.randint(0, 1)
        num = 2
        d = {
            0: self.path_sum_by_dfs,
            1: self.path_sum_by_dfs_postorder,
            2: self.path_sum_by_dfs_preorder,
        }

        return d[num](root, targetSum)

    def path_sum_by_dfs_preorder(self, root: TreeNode, targetSum: int) -> bool:
        ans = []
        stack = [(root, [root.val])]
        while len(stack) > 0:
            node, path_list = stack.pop()
            if node.left is None and node.right is None and sum(path_list) == targetSum:
                ans .append(path_list)

            if node.right is not None:
                stack.append((node.right, path_list + [node.right.val]))
            if node.left is not None:
                stack.append((node.left, path_list + [node.left.val]))
        return ans

    def path_sum_by_dfs_postorder(self, root: TreeNode, targetSum: int) -> bool:
        ans = []
        node = root
        stack = []
        pre_node = None
        path_list = []
        while True:
            while node is not None:
                path_list.append(node.val)
                stack.append(node)
                node = node.left
            if len(stack) <= 0:
                break
            if stack[-1].right != pre_node:
                node = stack[-1].right
                pre_node = None
            else:
                pre_node = stack.pop()
                if pre_node.left is None and pre_node.right is None and sum(path_list) == targetSum:
                    ans .append(path_list[:])
                path_list.pop()
        return ans

    def path_sum_by_dfs(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ans = []

        def dfs(node: TreeNode, path_list: List[int]):
            if node is None:
                return
            if node.left is None and node.right is None:
                if sum(path_list) + node.val == targetSum:
                    path_list.append(node.val)
                    ans .append(path_list)
                return

            path_list.append(node.val)
            dfs(node.left, path_list[:])
            dfs(node.right, path_list[:])

        dfs(root, [])
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22, [[5, 4, 11, 2], [5, 8, 4, 5]]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, target, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.pathSum(root, target)
            self.assertEqual(answer,ans )


if __name__ == '__main__':
    unittest.main()
