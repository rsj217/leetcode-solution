package g_121_best_time_to_buy_and_sell_stock

import "testing"

func Test_maxProfit(t *testing.T) {
	type args struct {
		prices []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "[7, 1, 5, 3, 6, 4]",
			args: args{[]int{7, 1, 5, 3, 6, 4}},
			want: 7,
		},
		{
			name: "[7, 6, 4, 3, 1]",
			args: args{[]int{7, 6, 4, 3, 1}},
			want: 0,
		},
		{
			name: "[4, 5]",
			args: args{[]int{4, 5}},
			want: 1,
		},
		{
			name: "[7]",
			args: args{[]int{7}},
			want: 0,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxProfit(tt.args.prices); got != tt.want {
				t.Errorf("maxProfit() = %v, want %v", got, tt.want)
			}
		})
	}
}
