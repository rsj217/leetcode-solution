from typing import List
from datastruct.treenode import TreeNode
import unittest


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        return list(self._levelOrder(root))

    def _levelOrder(self, root: TreeNode):
        if root is None:
            return
        node = root
        queue = [node]
        size = len(queue)
        while size > 0:
            level_nodes = []
            # 当前层节点大小
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                level_nodes.append(node.val)
                # 左子树进队
                if node.left is not None:
                    queue.append(node.left)
                # 右子树进队
                if node.right is not None:
                    queue.append(node.right)
            # 此层遍历完，进入下一层循环
            yield level_nodes


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_case = [
            ([3, 9, 20, None, None, 15, 7], [
                [3],
                [9, 20],
                [15, 7]
            ]),
        ]
        self.s = Solution()

    def test_solution(self):
        for nums, answer in self.test_case:
            root = TreeNode.create(nums)
            ans = self.s.levelOrder(root)
            # self.assertEqual(answer,ans )


if __name__ == '__main__':
    unittest.main()
