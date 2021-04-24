package g_100_same_tree

import (
	. "leetcode/datastruct"
)

func maxDepth(root *TreeNode) int {
	return maxDepthIter(root)
}

func maxDepthRecursion(root *TreeNode) int {
	if root == nil {
		return 0
	}
	left := maxDepthRecursion(root.Left)
	right := maxDepthRecursion(root.Right)
	max := left
	if left < right {
		max = right
	}
	return 1 + max
}

func maxDepthIter(root *TreeNode) int {
	if root == nil {
		return 0
	}

	queue := make([]*TreeNode, 1, 10)
	queue[0] = root
	deep := 0
	for len(queue) > 0 {
		deep += 1
		tmpQueue := make([]*TreeNode, 0, 10)
		for _, node := range queue {
			if node.Left != nil {
				tmpQueue = append(tmpQueue, node.Left)
			}
			if node.Right != nil {
				tmpQueue = append(tmpQueue, node.Right)
			}
		}
		queue = tmpQueue
	}
	return deep
}
