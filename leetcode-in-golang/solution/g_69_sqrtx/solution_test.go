package g_69_sqrtx

import "testing"

func Test_mySqrt(t *testing.T) {
	type args struct {
		x int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "0",
			args: args{0},
			want: 0,
		},
		{
			name: "1",
			args: args{1},
			want: 1,
		},
		{
			name: "2",
			args: args{2},
			want: 1,
		},
		{
			name: "4",
			args: args{4},
			want: 2,
		},
		{
			name: "8",
			args: args{8},
			want: 2,
		},
		{
			name: "15",
			args: args{15},
			want: 3,
		},
		{
			name: "17",
			args: args{17},
			want: 4,
		},
		{
			name: "2147395599",
			args: args{2147395599},
			want: 46339,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := mySqrt(tt.args.x); got != tt.want {
				t.Errorf("mySqrt() = %v, want %v", got, tt.want)
			}
		})
	}
}
