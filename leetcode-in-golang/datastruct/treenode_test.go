package datastruct

import (
	"reflect"
	"testing"
)

//node1 := NewTreeNode(1)
//node2 := NewTreeNode(2)
//node3 := NewTreeNode(3)
//node4 := NewTreeNode(4)
//node5 := NewTreeNode(5)
//node6 := NewTreeNode(6)

func treeNode1() *TreeNode {
	root := NewTreeNode(1)
	node2 := NewTreeNode(2)
	node3 := NewTreeNode(3)
	root.Left = node2
	root.Right = node3
	return root
}

func treeNode2() *TreeNode {
	root := NewTreeNode(1)
	node2 := NewTreeNode(2)
	node3 := NewTreeNode(3)
	root.Right = node2
	node2.Left = node3
	return root
}

func treeNode3() *TreeNode {
	root := NewTreeNode(1)
	node2 := NewTreeNode(2)
	node3 := NewTreeNode(3)
	node4 := NewTreeNode(4)
	node5 := NewTreeNode(5)
	root.Left = node2
	root.Right = node3
	node2.Right = node4
	node3.Left = node5
	return root
}

func treeNode4() *TreeNode {
	root := NewTreeNode(1)
	node2 := NewTreeNode(2)
	node3 := NewTreeNode(3)
	node5 := NewTreeNode(5)
	root.Left = node2
	root.Right = node3
	node3.Left = node5
	return root
}

func treeNode5() *TreeNode {
	root := NewTreeNode(1)
	node2 := NewTreeNode(2)
	node3 := NewTreeNode(3)
	node5 := NewTreeNode(5)
	node6 := NewTreeNode(6)
	root.Left = node2
	root.Right = node3
	node3.Left = node5
	node5.Left = node6
	return root
}

func TestCreate(t *testing.T) {
	type args struct {
		nums []interface{}
	}

	tests := []struct {
		name string
		args args
		want *TreeNode
	}{
		{
			name: "[]",
			args: args{nil},
			want: nil,
		},

		{
			name: "[1, 2, 3]",
			args: args{[]interface{}{1, 2, 3}},
			want: treeNode1(),
		},
		{
			name: "[1, nil, 2, 3]",
			args: args{[]interface{}{1, nil, 2, 3}},
			want: treeNode2(),
		},
		{
			name: "[1, 2, 3, nil, 4, 5]",
			args: args{[]interface{}{1, 2, 3, nil, 4, 5}},
			want: treeNode3(),
		},
		{
			name: "[1, 2, 3, nil, nil, 5]",
			args: args{[]interface{}{1, 2, 3, nil, nil, 5}},
			want: treeNode4(),
		},
		{
			name: "[1, 2, 3, nil, nil, 5, nil, 6]",
			args: args{[]interface{}{1, 2, 3, nil, nil, 5, nil, 6}},
			want: treeNode5(),
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Create(tt.args.nums); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("Create() = %v, want %v", got, tt.want)
			}
		})
	}
}
