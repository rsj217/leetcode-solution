package datastruct

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func NewTreeNode(val int) *TreeNode {
	return &TreeNode{Val: val}
}

func (n *TreeNode) HasLeft() bool {
	return n.Left != nil
}
func (n *TreeNode) HasRight() bool {
	return n.Right != nil
}

func (n *TreeNode) getHeight(node *TreeNode) int {
	if node == nil {
		return -1
	}
	leftHeight := node.getHeight(node.Left)
	rightHeight := node.getHeight(node.Right)
	if leftHeight < rightHeight {
		return 1 + rightHeight
	}
	return 1 + leftHeight
}

func (node *TreeNode) Height() int {
	return node.getHeight(node)
}

func Create(nums []interface{}) *TreeNode {
	size := len(nums)
	if size <= 0 {
		return nil
	}

	val := nums[0].(int)
	root := NewTreeNode(val)
	queue := make([]*TreeNode, 0, len(nums))
	queue = append(queue, root)
	index := 0
	for 0 < len(queue) {
		tempQueue := make([]*TreeNode, 0, len(nums))
		for i, _ := range queue {
			index++
			if 2*index-1 < size && nums[2*index-1] != nil {
				queue[i].Left = NewTreeNode(nums[2*index-1].(int))
				tempQueue = append(tempQueue, queue[i].Left)
			}
			if 2*index < size && nums[2*index] != nil {
				queue[i].Right = NewTreeNode(nums[2*index].(int))
				tempQueue = append(tempQueue, queue[i].Right)
			}
		}
		queue = tempQueue
	}
	return root
}

func PrintTree(root *TreeNode, width string) string {
	if root == nil {
		return ""
	}

	return ""
}
