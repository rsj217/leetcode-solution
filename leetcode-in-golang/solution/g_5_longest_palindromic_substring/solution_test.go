package g_5_longest_palindromic_substring

import "testing"

func Test_longestPalindrome(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			name: "empty string",
			args: args{""},
			want: "",
		},
		{
			name: "single string",
			args: args{"a"},
			want: "a",
		},
		{
			name: "double string",
			args: args{"aa"},
			want: "aa",
		},
		{
			name: "double string",
			args: args{"ab"},
			want: "a",
		},
		{
			name: "double string",
			args: args{"babad"},
			want: "bab",
		},
		{
			name: "normal string",
			args: args{"cbbd"},
			want: "bb",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := longestPalindrome(tt.args.s); got != tt.want {
				t.Errorf("longestPalindrome() = %v, want %v", got, tt.want)
			}
		})
	}
}
