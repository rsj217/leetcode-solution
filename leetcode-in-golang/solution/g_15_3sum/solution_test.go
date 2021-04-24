package g_15_3sum

import "testing"

func Test_threeSum(t *testing.T) {
	type args struct {
		x []int
	}
	tests := []struct {
		name string
		args args
		want [][]int
	}{
		{
			name: "[-1, 0, 1, 2, -1, -4]",
			args: args{[]int{-1, 0, 1, 2, -1, -4}},
			want: [][]int{{-1, -1, 2}, {-1, 0, 1}},
		},
		{
			name: "[1,2,-2,-1]",
			args: args{[]int{1, 2, -2, -1}},
			want: [][]int{},
		},
		{
			name: "[]",
			args: args{[]int{}},
			want: [][]int{},
		},
		{
			name: "[0]",
			args: args{[]int{0}},
			want: [][]int{},
		},
		{
			name: "[0, 0]",
			args: args{[]int{0, 0}},
			want: [][]int{},
		},
		{
			name: "[0, 0, 0, 0]",
			args: args{[]int{0, 0, 0, 0}},
			want: [][]int{{0, 0, 0}},
		},
		{
			name: "[-1, -1, 0, 1]",
			args: args{[]int{-1, -1, 0, 1}},
			want: [][]int{{-1, 0, 1}},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := threeSum(tt.args.x); !compareNestSlice(got, tt.want) {
				t.Errorf("threeSum() = %v, want %v", got, tt.want)
			}
		})
	}
}

func compareSlice(a, b []int) bool {
	for i, v := range a {
		if v != b[i] {
			return false
		}
	}
	return true
}

func compareNestSlice(a, b [][]int) bool {
	for i, v := range a {
		if !compareSlice(v, b[i]) {
			return false
		}
	}
	return true
}
