from typing import List
from datastruct.treenode import TreeNode
import unittest


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(inorder) <= 0:
            return None
        root_val = preorder[0]
        root = TreeNode(val=root_val)

        index = inorder.index(root_val)

        inorder_left = inorder[0:index]      # [0, root) root=index -> [0, index)
        inorder_right = inorder[index + 1:]  # [root+1, len(inorder))  ->[index+1, )

        preorder_left = preorder[1:index + 1] # [1:1+len(inorder_left))   -> [1, index+1)
        preorder_right = preorder[index + 1:] # [index+1: len(inorder_right] -> [index+1, )

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        return root


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]),
        ]
        self.s = Solution()

    def test_solution(self):
        for preorder, inorder in self.test_case:
            ans = self.s.buildTree(preorder, inorder)

            # self.assertEqual(answer,ans )


if __name__ == '__main__':
    unittest.main()
