package g_81_search_in_rotated_sorted_array_ii

import "testing"

func Test_searchII(t *testing.T) {
	type args struct {
		nums   []int
		target int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "[2, 5, 6, 0, 0, 1, 2]",
			args: args{[]int{2, 5, 6, 0, 0, 1, 2}, 0},
			want: true,
		},
		{
			name: "[2, 5, 6, 0, 0, 1, 2]",
			args: args{[]int{2, 5, 6, 0, 0, 1, 2}, 3},
			want: false,
		},
		{
			name: "[1, 0, 1, 1, 1]",
			args: args{[]int{1, 0, 1, 1, 1}, 0},
			want: true,
		},
		{
			name: "[1, 0, 1, 1, 1]",
			args: args{[]int{1, 0, 1, 2, 1}, 2},
			want: true,
		},
		{
			name: "[5, 1, 3]",
			args: args{[]int{5, 1, 3}, 3},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := searchII(tt.args.nums, tt.args.target); got != tt.want {
				t.Errorf("search() = %v, want %v", got, tt.want)
			}
		})
	}
}
