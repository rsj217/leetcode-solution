package g_704_binary_search

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
			name: "[-1,0,3,5,9,12], 9",
			args: args{[]int{-1, 0, 3, 5, 9, 12}, 9},
			want: 4,
		},
		{
			name: "[-1,0,3,5,9,12], 2",
			args: args{[]int{-1, 0, 3, 5, 9, 12}, 2},
			want: -1,
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
