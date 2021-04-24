package g_7_reverse_integer

import "testing"

func Test_reverse(t *testing.T) {
	type args struct {
		x int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "123",
			args: args{123},
			want: 321,
		},
		{
			name: "-123",
			args: args{-123},
			want: -321,
		},
		{
			name: "0",
			args: args{0},
			want: 0,
		},
		{
			name: "2147483647",
			args: args{2147483647},
			want: 0,
		},
		{
			name: "1463847412",
			args: args{1463847412},
			want: 2147483641,
		},
		{
			name: "1463847413",
			args: args{1463847413},
			want: 0,
		},
		{
			name: "1534236469",
			args: args{1534236469},
			want: 0,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := reverse(tt.args.x); got != tt.want {
				t.Errorf("reverse() = %v, want %v", got, tt.want)
			}
		})
	}
}
