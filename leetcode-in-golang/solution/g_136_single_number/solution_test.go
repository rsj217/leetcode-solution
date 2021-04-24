package g_136_single_number

import "testing"

func Test_singleNumber(t *testing.T) {
	type args struct {
		x []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "2,2,1",
			args: args{[]int{2, 2, 1}},
			want: 1,
		},
		{
			name: "4,1,2,1,2",
			args: args{[]int{4, 1, 2, 1, 2}},
			want: 4,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := singleNumber(tt.args.x); got != tt.want {
				t.Errorf("singleNumber() = %v, want %v", got, tt.want)
			}
		})
	}
}
