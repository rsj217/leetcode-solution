package g_94_binary_tree_inorder_traversal

import (
	. "leetcode/datastruct"
	"reflect"
	"testing"
)

func Test_inorderTraversalRecursion(t *testing.T) {
	type args struct {
		root *TreeNode
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := inorderTraversalRecursion(tt.args.root); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("inorderTraversalRecursion() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_inorderTraversalRecursion1(t *testing.T) {
	type args struct {
		root *TreeNode
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := inorderTraversalRecursion(tt.args.root); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("inorderTraversalRecursion() = %v, want %v", got, tt.want)
			}
		})
	}
}
