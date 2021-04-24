package g_35_search_insert_position

import "testing"

func Test_searchInsertPosition(t *testing.T) {
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
			name: "[1,3,4,6] 0",
			args: args{[]int{1, 3, 4, 6}, 1},
			want: 0,
		},
		{
			name: "[1,3,4,6] 2",
			args: args{[]int{1, 3, 4, 6}, 2},
			want: 1,
		},
		{
			name: "[1,3,4,6] 5",
			args: args{[]int{1, 3, 4, 6}, 5},
			want: 3,
		},
		{
			name: "[1,3,4,6] 7",
			args: args{[]int{1, 3, 4, 6}, 7},
			want: 4,
		},
		{
			name: "[4,5,5,5] 5",
			args: args{[]int{4, 5, 5, 5}, 5},
			want: 1,
		},
		{
			name: "[5,5,5,5] 5",
			args: args{[]int{5, 5, 5, 5}, 5},
			want: 0,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := searchInsert(tt.args.nums, tt.args.target); got != tt.want {
				t.Errorf("searchInsert() = %v, want %v", got, tt.want)
			}
		})
	}
}
