from datastruct.linknode import ListNode
import unittest


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode(0)
        node = head
        while l1 is not None or l2 is not None or carry != 0:
            sum_ = carry
            if l1 is not None:
                sum_ += l1.val
                l1 = l1.next
            if l2 is not None:
                sum_ += l2.val
                l2 = l2.next

            carry = sum_ // 10
            node.next = ListNode(sum_ % 10)
            node = node.next
        return head.next


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_normal(self):
        l1 = [2, 4, 3]
        l2 = [5, 6, 4]
        answer = [7, 0, 8]
        l1 = ListNode.create(l1)
        l2 = ListNode.create(l2)
        ans = self.s.addTwoNumbers(l1, l2)
        self.assertEqual(answer,ans .to_list())

    def test_99999(self):
        l1 = [9, 9, 9, 9, 9, 9, 9]
        l2 = [9, 9, 9, 9]
        answer = [8, 9, 9, 9, 0, 0, 0, 1]
        l1 = ListNode.create(l1)
        l2 = ListNode.create(l2)
        ans = self.s.addTwoNumbers(l1, l2)
        self.assertEqual(answer,ans .to_list())


if __name__ == '__main__':
    unittest.main()
