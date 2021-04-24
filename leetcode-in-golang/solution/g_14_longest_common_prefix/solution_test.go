package g_14_longest_common_prefix

import "testing"

func Test_longestCommonPrefix(t *testing.T) {
	type args struct {
		x []string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			name: "[\"flower\",\"flow\",\"flight\"]",
			args: args{[]string{"flower", "flow", "flight"}},
			want: "fl",
		},
		{
			name: "[\"dog\", \"racecar\", \"car\"]",
			args: args{[]string{"dog", "racecar", "car"}},
			want: "",
		},
		{
			name: "[\"\", \"\", \"\"]",
			args: args{[]string{"", "", ""}},
			want: "",
		},
		{
			name: "[\"\", \"qwe\"]",
			args: args{[]string{"", "qwe"}},
			want: "",
		},
		{
			name: "[\"\", \"qwe\"]",
			args: args{[]string{"", "qwe"}},
			want: "",
		},
		{
			name: "[]",
			args: args{[]string{}},
			want: "",
		},
		{
			name: "[\"a\"]",
			args: args{[]string{"a"}},
			want: "a",
		},
		{
			name: "[\"abc\", \"abc\"]",
			args: args{[]string{"abc", "abc"}},
			want: "abc",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := longestCommonPrefix1(tt.args.x); got != tt.want {
				t.Errorf("longestCommonPrefix1() = %v, want %v", got, tt.want)
			}
		})
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := longestCommonPrefix(tt.args.x); got != tt.want {
				t.Errorf("longestCommonPrefix() = %v, want %v", got, tt.want)
			}
		})
	}
}
