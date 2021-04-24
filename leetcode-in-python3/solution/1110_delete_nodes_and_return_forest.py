from typing import List
from datastruct.treenode import TreeNode
import unittest
import random


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:

        num = random.randint(0, 1)
        d = {
            0: self.postorder,
            1: self.dfs,
        }
        return d[num](root, to_delete)

    def postorder(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if root is None:
            return []

        t = {}

        ans = []
        stack = []
        visited = None
        node = root

        head = TreeNode(val=None)
        head.left = node

        parent = head
        position = "l"
        while True:
            while node is not None:
                stack.append((node, parent, position))
                parent = node
                position = "l"
                node = node.left
            if len(stack) <= 0:
                break
            if stack[-1][0].right != visited:
                node = stack[-1][0].right
                parent = stack[-1][0]
                position = "r"
                visited = None
            else:
                visited, parent, position = stack.pop()
                for i in to_delete:
                    if t.get(i, False):
                        continue

                    if visited.val == i:
                        if visited.left is not None:
                            ans .append(visited.left)
                            visited.left = None
                        if visited.right is not None:
                            ans .append(visited.right)
                            visited.right = None
                        # 处理parent
                        if position == "l":
                            parent.left = None
                        else:
                            parent.right = None
                        t[i] = True

        if head.left is not None:
            ans .append(head.left)
            head.left = None
        return ans

    def dfs(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans = []
        t = {}

        def _dfs(node: TreeNode, parent: TreeNode, position: str):
            if node is None:
                return

            _dfs(node.left, node, "l")
            _dfs(node.right, node, "r")

            for i in to_delete:
                if t.get(i, False):
                    continue
                if i == node.val:
                    if node.left is not None:
                        ans .append(node.left)
                        node.left = None
                    if node.right is not None:
                        ans .append(node.right)
                        node.right = None

                    if position == "l":
                        parent.left = None
                    else:
                        parent.right = None
                    t[i] = True

        # 处理 root
        parent = TreeNode(val=None)
        parent.left = root
        _dfs(root, parent, "l")
        if parent.left is not None:
            ans .append(parent.left)
            parent.left = None
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([1, 2, 4, None, 3], [3, 5], [])
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, target, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.delNodes(root, target)  # TODO
            # self.assertEqual(answer,ans , (nums, answer))


if __name__ == '__main__':
    unittest.main()
