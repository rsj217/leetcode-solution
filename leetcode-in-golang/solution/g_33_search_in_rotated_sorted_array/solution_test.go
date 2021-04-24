package g_33_search_in_rotated_sorted_array

import "testing"

func Test_search(t *testing.T) {
	type args struct {
		nums   []int
		target int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "[4, 5, 6, 7, 0, 1, 2]",
			args: args{[]int{4, 5, 6, 7, 0, 1, 2}, 0},
			want: 4,
		},
		{
			name: "[4, 5, 6, 7, 0, 1, 2]",
			args: args{[]int{}, 3},
			want: -1,
		},
		{
			name: "[1]",
			args: args{[]int{1}, 0},
			want: -1,
		},
		{
			name: "[5]",
			args: args{[]int{5}, 1},
			want: -1,
		},
		{
			name: "[5]",
			args: args{[]int{5}, 5},
			want: 0,
		},
		{
			name: "[4, 5]",
			args: args{[]int{4, 5}, 3},
			want: -1,
		},
		{
			name: "[4, 5]",
			args: args{[]int{4, 5}, 4},
			want: 0,
		},
		{
			name: "[4, 5]",
			args: args{[]int{4, 5}, 5},
			want: 1,
		},
		{
			name: "[4, 5]",
			args: args{[]int{4, 5}, 6},
			want: -1,
		},
		{
			name: "[5, 4]",
			args: args{[]int{5, 4}, 0},
			want: -1,
		},
		{
			name: "[5, 4]",
			args: args{[]int{5, 4}, 4},
			want: 1,
		},
		{
			name: "[5, 4]",
			args: args{[]int{5, 4}, 5},
			want: 0,
		},
		{
			name: "[5, 4]",
			args: args{[]int{5, 4}, 10},
			want: -1,
		},
		{
			name: "[5, 6, 2, 3]",
			args: args{[]int{5, 6, 2, 3}, 2},
			want: 2,
		},
		{
			name: "[6, 7, 0, 2, 3]",
			args: args{[]int{6, 7, 0, 2, 3}, 2},
			want: 3,
		},
		{
			name: "[6, 7, 1, 2, 3]",
			args: args{[]int{6, 7, 1, 2, 3}, 7},
			want: 1,
		},
		{
			name: "[6, 7, 1, 2, 3]",
			args: args{[]int{6, 7, 1, 2, 3}, 6},
			want: 0,
		},
		{
			name: "[6, 7, 1, 2, 3]",
			args: args{[]int{6, 7, 1, 2, 3}, 6},
			want: 0,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := search(tt.args.nums, tt.args.target); got != tt.want {
				t.Errorf("search() = %v, want %v", got, tt.want)
			}
		})
	}
}
