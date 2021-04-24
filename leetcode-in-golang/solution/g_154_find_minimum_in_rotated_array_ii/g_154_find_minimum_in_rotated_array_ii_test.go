package g_154_find_minimum_in_rotated_array_ii

import "testing"

func Test_findMin(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "[3, 4, 5, 1, 2]",
			args: args{[]int{3, 4, 5, 1, 2}},
			want: 1,
		},
		{
			name: "[4, 5, 6, 7, 0, 1, 2]",
			args: args{[]int{4, 5, 6, 7, 0, 1, 2}},
			want: 0,
		},
		{
			name: "[5]",
			args: args{[]int{5}},
			want: 5,
		},
		{
			name: "[4, 5]",
			args: args{[]int{4, 5}},
			want: 4,
		},
		{
			name: "[5, 4]",
			args: args{[]int{5, 4}},
			want: 4,
		},
		{
			name: "[6, 7, 1, 2, 3]",
			args: args{[]int{6, 7, 1, 2, 3}},
			want: 1,
		},
		{
			name: "[4, 0, 3]",
			args: args{[]int{4, 0, 3}},
			want: 0,
		},
		{
			name: "[2,2,2,0,1]",
			args: args{[]int{2, 2, 2, 0, 1}},
			want: 0,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := findMin(tt.args.nums); got != tt.want {
				t.Errorf("findMin() = %v, want %v", got, tt.want)
			}
		})
	}
}
