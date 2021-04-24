from datastruct.treenode import TreeNode
import unittest


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        prev = TreeNode(val=float("-inf"))
        node = root
        stack = []
        while True:
            while node is not None:
                stack.append(node)
                node = node.left
            if not stack:
                break
            node = stack.pop()
            if node.val <= prev.val:
                return False
            prev = node
            node = node.right
        return True


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([2, 1, 3], True),
            ([1, 1], False),
            ([5, 1, 4, None, None, 3, 6], False),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.isValidBST(root)
            self.assertEqual(answer,ans )


if __name__ == '__main__':
    unittest.main()
