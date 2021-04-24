package g_13_roman_to_integer

import "testing"

func Test_romanToInt(t *testing.T) {
	type args struct {
		x string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "3",
			args: args{"III"},
			want: 3,
		},
		{
			name: "4",
			args: args{"IV"},
			want: 4,
		},
		{
			name: "9",
			args: args{"IX"},
			want: 9,
		},
		{
			name: "58",
			args: args{"LVIII"},
			want: 58,
		},
		{
			name: "1994",
			args: args{"MCMXCIV"},
			want: 1994,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := romanToInt(tt.args.x); got != tt.want {
				t.Errorf("romanToInt() = %v, want %v", got, tt.want)
			}
		})
	}
}
