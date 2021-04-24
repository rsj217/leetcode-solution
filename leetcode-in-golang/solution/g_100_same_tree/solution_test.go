package g_100_same_tree

import (
	. "leetcode/datastruct"
	"testing"
)

func Test_isSameTree(t *testing.T) {
	type args struct {
		p *TreeNode
		q *TreeNode
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "[1, 2, 3] [1, 2, 3]",
			args: args{Create([]interface{}{1, 2, 3}), Create([]interface{}{1, 2, 3})},
			want: true,
		},
		{
			name: "[1, 2] [1, nil 2]",
			args: args{Create([]interface{}{1, 2}), Create([]interface{}{1, nil, 2})},
			want: false,
		},
		{
			name: "[1, 2, 1] [1, 1, 2]",
			args: args{Create([]interface{}{1, 2, 1}), Create([]interface{}{1, 1, 2})},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isSameTree(tt.args.p, tt.args.q); got != tt.want {
				t.Errorf("isSameTree() = %v, want %v", got, tt.want)
			}
		})
	}
}
