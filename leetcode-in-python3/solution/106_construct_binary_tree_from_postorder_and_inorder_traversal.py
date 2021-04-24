from typing import List
from datastruct.treenode import TreeNode, print_tree
import unittest


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) <= 0:
            return None

        root_val = postorder[-1]
        root = TreeNode(val=root_val)

        index = inorder.index(root_val)

        inorder_left = inorder[0:index]
        inorder_right = inorder[index + 1:]

        postorder_left = postorder[0:index]
        postorder_right = postorder[index:len(postorder) - 1]

        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3],),
        ]
        self.s = Solution()

    def test_solution(self):
        for inorder, postorder in self.test_case:
            ans = self.s.buildTree(inorder, postorder)

            print(print_tree(ans ))
            # self.assertEqual(answer,ans )


if __name__ == '__main__':
    unittest.main()
