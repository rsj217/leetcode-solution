package g_100_same_tree

import (
	. "leetcode/datastruct"
)

func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}
	return isSymmetricTwoNode(root.Left, root.Right)
}

func isSymmetricTwoNode(p, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	} else if p == nil || q == nil {
		return false
	} else { // p != nil && q != nil
		return p.Val == q.Val && isSymmetricTwoNode(p.Left, q.Right) && isSymmetricTwoNode(p.Right, q.Left)
	}

}
