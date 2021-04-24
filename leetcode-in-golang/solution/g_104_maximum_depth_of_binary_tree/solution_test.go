package g_100_same_tree

import (
	. "leetcode/datastruct"
	"testing"
)

func Test_maxDepth(t *testing.T) {
	type args struct {
		root *TreeNode
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "[3, 9, 20, Nil, Nil, 15, 7]",
			args: args{Create([]interface{}{3, 9, 20, nil, nil, 15, 7})},
			want: 3,
		},
		{
			name: "[]",
			args: args{Create([]interface{}{})},
			want: 0,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxDepth(tt.args.root); got != tt.want {
				t.Errorf("maxDepth() = %v, want %v", got, tt.want)
			}
		})
	}
}
