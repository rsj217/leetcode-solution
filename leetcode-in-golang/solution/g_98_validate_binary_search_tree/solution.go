package g_98_validate_binary_search_tree

import (
	. "leetcode/datastruct"
)

func isValidBST(root *TreeNode) bool {
	node := root
	var prev *TreeNode
	stack := make([]*TreeNode, 0, 10)
	for {
		for node != nil {
			stack = append(stack, node)
			node = node.Left
		}

		if len(stack) <= 0 {
			break
		}
		node = stack[len(stack)-1]
		if prev != nil {
			if node.Val <= prev.Val {
				return false
			}
		}
		prev = node
		node = node.Right
		stack = stack[0 : len(stack)-1]
	}
	return true
}
