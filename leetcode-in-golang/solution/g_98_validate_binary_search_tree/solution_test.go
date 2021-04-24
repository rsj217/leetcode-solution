package g_98_validate_binary_search_tree

import (
	. "leetcode/datastruct"
	"testing"
)

func Test_isValidBST(t *testing.T) {
	type args struct {
		root *TreeNode
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "[]",
			args: args{Create([]interface{}{})},
			want: true,
		},
		{
			name: "[-2147483648]",
			args: args{Create([]interface{}{-2147483648})},
			want: true,
		},
		{
			name: "[2, 1, 3]",
			args: args{Create([]interface{}{2, 1, 3})},
			want: true,
		},
		{
			name: "[1, 1]",
			args: args{Create([]interface{}{1, 1})},
			want: false,
		},
		{
			name: "[5, 1, 4, nil, nil, 3, 6]",
			args: args{Create([]interface{}{5, 1, 4, nil, nil, 3, 6})},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isValidBST(tt.args.root); got != tt.want {
				t.Errorf("isValidBST() = %v, want %v", got, tt.want)
			}
		})
	}
}
