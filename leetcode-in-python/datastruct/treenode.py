from typing import List
from collections import deque
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        cur = self.val
        left = self.left.val if self.left is not None else ""
        right = self.right.val if self.right is not None else ""
        return f"{left}<-{cur}->{right}"

    def __repr__(self):
        return self.__str__()

    @property
    def has_left(self):
        return self.left is not None

    @property
    def has_right(self):
        return self.right is not None

    @property
    def height(self):
        return self._get_height(self)

    def _get_height(self, node) -> int:
        if not node:
            return -1
        return 1 + max(self._get_height(node.left), self._get_height(node.right))

    @classmethod
    def create(cls, nums: List[int]):
        nums_size = len(nums)
        if nums_size <= 0:
            return None

        root = cls(nums[0])
        queue = deque()
        queue.append(root)
        index = 0
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                index += 1
                node = queue.popleft()
                if 2 * index - 1 < nums_size and nums[2 * index - 1] is not None:
                    node.left = cls(nums[2 * index - 1])
                    queue.append(node.left)
                if 2 * index < nums_size and nums[2 * index] is not None:
                    node.right = cls(nums[2 * index])
                    queue.append(node.right)
        return root


def print_tree(node, width=' ') -> str:
    if node is None:
        return ''

    root_height, deep = node.height, 0
    levels = []
    q = [(node, 1)]
    while q:
        level = []
        pre_index = 0
        step = 2 ** (root_height - deep + 1)
        start = 2 ** (root_height - deep) - 1
        deep += 1
        size = len(q)
        for index in range(size):
            node, seq = q.pop(0)
            arr_index = start + (seq - 1) * step
            space = width * arr_index if index == 0 else width * (arr_index - pre_index - 1)

            s = f'{space}{node.val}'
            level.append(s)
            if index == size - 1:
                level.append('\n\n')
            if node.has_left:
                q.append((node.left, 2 * seq - 1))
            if node.has_right:
                q.append((node.right, 2 * seq))
            pre_index = arr_index
        levels.append(''.join(level))
    return ''.join(levels)


def tree_deep(node: TreeNode) -> int:
    max_deep = 0

    def dfs(node: TreeNode, level: int):
        nonlocal max_deep
        if node is None:
            return
        max_deep = max(max_deep, level)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(node, 0)
    return max_deep


def tree_literal(node: TreeNode) -> List[int]:
    if node is None:
        return []
    max_deep = tree_deep(node)
    ret = [node.val]
    queue = [node]

    deep = -1
    while len(queue) > 0:
        size = len(queue)
        deep += 1
        for i in range(size):
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            if deep < max_deep:
                left, right = None, None
                if node.left is not None:
                    left = node.left.val
                if node.right is not None:
                    right = node.right.val
                ret.append(left)
                ret.append(right)

    for i in range(len(ret) - 1, -1, -1):
        if ret[i] is None:
            ret.pop()
        else:
            break
    return ret


class TestTreeNode(unittest.TestCase):

    def test_create(self):
        nums = []
        root = TreeNode.create(nums)
        self.assertIsNone(root)

        nums = [1, 2, 3]
        root = TreeNode.create(nums)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)

        self.assertEqual(nums, tree_literal(root))

        nums = [1, None, 2, 3]
        root = TreeNode.create(nums)
        self.assertEqual(root.val, 1)
        self.assertIsNone(root.left)
        self.assertEqual(root.right.val, 2)
        self.assertEqual(root.right.left.val, 3)

        self.assertEqual(nums, tree_literal(root))

        nums = [1, 2, 3, None, 4, 5]
        root = TreeNode.create(nums)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertIsNone(root.left.left)
        self.assertEqual(root.left.right.val, 4)
        self.assertEqual(root.right.left.val, 5)

        self.assertEqual(nums, tree_literal(root))

        nums = [1, 2, 3, None, None, 5]
        root = TreeNode.create(nums)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertIsNone(root.left.left)
        self.assertIsNone(root.left.right)
        self.assertEqual(root.right.left.val, 5)

        self.assertEqual(nums, tree_literal(root))

        nums = [1, 2, 3, None, None, 5, None, 6]
        root = TreeNode.create(nums)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertIsNone(root.left.left)
        self.assertIsNone(root.left.right)
        self.assertEqual(root.right.left.val, 5)
        self.assertIsNone(root.right.right)
        self.assertEqual(root.right.left.left.val, 6)

        self.assertEqual(nums, tree_literal(root))


class TestPrintTreeNode(unittest.TestCase):

    def test_empty(self):
        root = TreeNode.create([])
        print(print_tree(root))

    def test_print_tree(self):
        root = TreeNode.create([1, 2, None, 2, None, 3])
        root = TreeNode.create([1, 2, 3, 4, None, 5, 6, None, 7, None, None, 8])
        print(print_tree(root, " "))

        nums = [1, None, 2, 3]
        root = TreeNode.create(nums)
        print(print_tree(root, " "))

        nums = [1, 2, None, 3]
        root = TreeNode.create(nums)
        print(print_tree(root, " "))

        nums = [1, 2, 3, None, 4, 5]
        root = TreeNode.create(nums)
        print(print_tree(root, " "))

        nums = [1, 2, 3, None, None, 5]
        root = TreeNode.create(nums)
        print(print_tree(root, " "))

        nums = [1, 2, 3, None, None, 5, None, 6]
        root = TreeNode.create(nums)
        print(print_tree(root, " "))


if __name__ == '__main__':
    unittest.main()
