package g_1302_deepest_leaves_sum

import "testing"
import . "leetcode/datastruct"

func Test_deepestLeavesSum(t *testing.T) {
	type args struct {
		root *TreeNode
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "[1,2,3,4,5,nil,6,7,nil,nil,nil,nil,8]",
			args: args{Create([]interface{}{1, 2, 3, 4, 5, nil, 6, 7, nil, nil, nil, nil, 8})},
			want: 15,
		},
		{
			name: "[6,7,8,2,7,1,3,9,nil,1,4,nil,nil,nil,5]",
			args: args{Create([]interface{}{6, 7, 8, 2, 7, 1, 3, 9, nil, 1, 4, nil, nil, nil, 5})},
			want: 19,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {

			if got := deepestLeavesSum(tt.args.root); got != tt.want {
				t.Errorf("deepestLeavesSum() = %v, want %v", got, tt.want)
			}
		})
	}
}
