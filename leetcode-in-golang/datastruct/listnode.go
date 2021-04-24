package datastruct

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func NewListNode(val int) *ListNode {
	return &ListNode{Val: val}
}

func (ln *ListNode) String() string {
	r := ""
	node := ln
	for node != nil {
		r += fmt.Sprintf("%d->", node.Val)
		node = node.Next
	}
	return r
}

func (ln *ListNode) ToSlice() []int {
	r := make([]int, 0, 10)
	node := ln
	for node != nil {
		r = append(r, node.Val)
		node = node.Next
	}
	return r
}

func CreateListNode(nums []int) *ListNode {
	if len(nums) <= 0 {
		return nil
	}
	head := NewListNode(nums[0])
	node := head
	for _, v := range nums[1:] {
		node.Next = NewListNode(v)
		node = node.Next
	}
	return head
}
