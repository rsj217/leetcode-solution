package g_1302_deepest_leaves_sum

import . "leetcode/datastruct"

var (
	maxVal   = 0
	maxLevel = 0
)

func deepestLeavesSum(root *TreeNode) int {
	maxVal = 0
	maxLevel = 0
	dfs(root, 0)
	return maxVal
}

func dfs(node *TreeNode, curLevel int) {
	if node == nil {
		return
	}
	if node.Left == nil && node.Right == nil {
		if maxLevel < curLevel {
			maxLevel = curLevel
			maxVal = node.Val
		} else if maxLevel == curLevel {
			maxVal += node.Val
		}
	}
	dfs(node.Left, curLevel+1)
	dfs(node.Right, curLevel+1)
}
