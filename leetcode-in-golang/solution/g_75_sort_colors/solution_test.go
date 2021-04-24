package g_75_sort_colors

import (
	"testing"
)

func Test_sortColors(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "[2,0,2,1,1,0]",
			args: args{[]int{2, 0, 2, 1, 1, 0}},
			want: []int{0, 0, 1, 1, 2, 2},
		},
		{
			name: "[2,0,1]",
			args: args{[]int{2, 0, 1}},
			want: []int{0, 1, 2},
		},
		{
			name: "[0, 1, 0]",
			args: args{[]int{0, 1, 0}},
			want: []int{0, 0, 1},
		},
		{
			name: "[0]",
			args: args{[]int{0}},
			want: []int{0},
		},
		{
			name: "[1]",
			args: args{[]int{1}},
			want: []int{1},
		},
		{
			name: "[2]",
			args: args{[]int{2}},
			want: []int{2},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			sortColors(tt.args.nums)
		})
	}
}
