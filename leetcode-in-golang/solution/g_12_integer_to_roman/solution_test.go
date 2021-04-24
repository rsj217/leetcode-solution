package g_12_integer_to_roman

import "testing"

func Test_intToRoman(t *testing.T) {
	type args struct {
		x int
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			name: "3",
			args: args{3},
			want: "III",
		},
		{
			name: "4",
			args: args{4},
			want: "IV",
		},
		{
			name: "9",
			args: args{9},
			want: "IX",
		},
		{
			name: "58",
			args: args{58},
			want: "LVIII",
		},
		{
			name: "1994",
			args: args{1994},
			want: "MCMXCIV",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := intToRoman(tt.args.x); got != tt.want {
				t.Errorf("intToRoman() = %v, want %v", got, tt.want)
			}
		})
	}
}
