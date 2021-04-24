from typing import List
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = ""
        node = self
        while node is not None:
            s += f"{node.val}->"
            node = node.next
        return s

    def to_list(self):
        node = self
        r = []
        while node is not None:
            r.append(node.val)
            node = node.next
        return r

    @classmethod
    def create(cls, nums: List[int]):
        if not nums:
            return None

        head = cls(val=nums[0])
        node = head
        for i in nums[1:]:
            node.next = cls(val=i)
            node = node.next
        return head


class TestListNode(unittest.TestCase):

    def test_create(self):
        nums = []
        node = ListNode.create(nums)
        self.assertIsNone(node)

        nums = [3]
        node = ListNode.create(nums)
        self.assertEqual(node.val, 3)
        self.assertIsNone(node.next)

        nums = [3, 5, 6]
        node = ListNode.create(nums)
        self.assertEqual(node.val, 3)
        self.assertEqual(node.next.val, 5)
        self.assertEqual(node.next.next.val, 6)
        self.assertIsNone(node.next.next.next)


if __name__ == '__main__':
    nums = [3, 5, 6, 2, 6]
    node = ListNode.create(nums)
    print(node)
