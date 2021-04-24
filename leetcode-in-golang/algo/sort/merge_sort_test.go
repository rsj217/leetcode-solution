package sort

import (
	"github.com/stretchr/testify/assert"
	"leetcode/util"
	"testing"
)

func TestMergeSort(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
	}{
		{
			name: "[]",
			args: args{[]int{}},
		},
		{
			name: "[0, 0, 0]",
			args: args{[]int{0, 0, 0}},
		},
		{
			name: "[0, 3, 1, 1]",
			args: args{[]int{0, 3, 1, 1}},
		},
		{
			name: "random(1000, 0, 100)",
			args: args{util.RandomNums(1000, 0, 100)},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			MergeSort(tt.args.nums)
			assert.True(t, util.IsSorted(tt.args.nums))
		})
	}
}
