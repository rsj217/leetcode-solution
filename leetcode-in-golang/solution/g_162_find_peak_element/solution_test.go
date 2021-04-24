package g_162_find_peak_element

import (
	"leetcode/util"
	"testing"
)

func Test_find_peak_element(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "[1, 2, 1, 3, 5, 6, 4]",
			args: args{[]int{1, 2, 1, 3, 5, 6, 4}},
			want: []int{1, 5},
		}, {

			name: "[1, 2, 3, 1]",
			args: args{[]int{1, 2, 3, 1}},
			want: []int{2},
		},
		{
			name: "[1, 2, 3]",
			args: args{[]int{1, 2, 3}},
			want: []int{2},
		},
		{
			name: "[3, 2, 1]",
			args: args{[]int{3, 2, 1}},
			want: []int{0},
		},
		{
			name: "[3]",
			args: args{[]int{3}},
			want: []int{0},
		},
		{
			name: "[3, 2]",
			args: args{[]int{3, 2}},
			want: []int{0},
		},
		{
			name: "[2,3]",
			args: args{[]int{2, 3}},
			want: []int{1}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := find_peak_element(tt.args.nums); !util.ContainInt(tt.want, got) {
				t.Errorf("find_peak_element() = %v, want %v", got, tt.want)
			}
		})
	}
}
