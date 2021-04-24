package g_9_palindrome_number

import "testing"

func Test_isPalindrome(t *testing.T) {
	type args struct {
		x int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "123",
			args: args{123},
			want: false,
		},
		{
			name: "121",
			args: args{121},
			want: true,
		},
		{
			name: "-121",
			args: args{-121},
			want: false,
		},
		{
			name: "0",
			args: args{0},
			want: true,
		},
		{
			name: "-0",
			args: args{-0},
			want: true,
		},
		{
			name: "1221",
			args: args{1221},
			want: true,
		},
		{
			name: "12321",
			args: args{12321},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isPalindrome(tt.args.x); got != tt.want {
				t.Errorf("isPalindrome() = %v, want %v", got, tt.want)
			}
		})
	}
}
