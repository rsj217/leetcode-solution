package g_2_add_two_numbers

import . "leetcode/datastruct"

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	carry := 0
	head := &ListNode{}
	node := head

	for l1 != nil || l2 != nil || carry != 0 {
		sum := carry
		if l1 != nil {
			sum += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			sum += l2.Val
			l2 = l2.Next
		}

		carry = sum / 10
		node.Next = &ListNode{Val: sum % 10}
		node = node.Next
	}
	return head.Next
}
