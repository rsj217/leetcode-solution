import random
from datastruct.treenode import TreeNode
import unittest


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        num = random.randint(0, 1)
        d = {
            0: self.dfs,
            1: self.postorder,
            2: self.bfs,
        }

        return d[num](root, targetSum)

    def bfs(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        stack = [(root, root.val)]
        while len(stack) > 0:
            node, path_sum = stack.pop()
            if node.left is None and node.right is None and path_sum == targetSum:
                return True
            if node.right is not None:
                stack.append((node.right, path_sum + node.right.val))
            if node.left is not None:
                stack.append((node.left, path_sum + node.left.val))
        return False

    def postorder(self, root: TreeNode, targetSum: int) -> bool:
        node = root
        stack = []
        pre_node = None
        path_sum = 0
        while True:
            while node is not None:
                path_sum += node.val
                stack.append(node)
                node = node.left
            if len(stack) <= 0:
                break
            if stack[-1].right != pre_node:
                node = stack[-1].right
                pre_node = None
            else:
                pre_node = stack.pop()
                if pre_node.left is None and pre_node.right is None and path_sum == targetSum:
                    return True
                path_sum -= pre_node.val
        return False

    def dfs(self, root: TreeNode, targetSum: int) -> bool:
        def _dfs(node: TreeNode, path_sum: int) -> bool:
            if node is None:
                return False
            if node.left is None and node.right is None:
                return path_sum + node.val == targetSum
            path_sum += node.val
            return _dfs(node.left, path_sum) or _dfs(node.right, path_sum)

        return _dfs(root, 0)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True),
            ([1, 2, 3], 5, False),
            ([], 1, False)
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, target, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.hasPathSum(root, target)
            self.assertEqual(answer, ans)


if __name__ == '__main__':
    unittest.main()
