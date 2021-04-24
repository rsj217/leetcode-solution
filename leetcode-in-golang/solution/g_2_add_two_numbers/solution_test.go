package g_2_add_two_numbers

import (
	. "leetcode/datastruct"
	"reflect"
	"testing"
)

func Test_addTwoNumbers(t *testing.T) {
	type args struct {
		l1 *ListNode
		l2 *ListNode
	}
	tests := []struct {
		name string
		args args
		want *ListNode
	}{
		{
			name: "2->4->3 + 5->6->4",
			args: args{CreateListNode([]int{2, 4, 3}), CreateListNode([]int{5, 6, 4})},
			want: CreateListNode([]int{7, 0, 8}),
		},
		{
			name: "9->9->9->9->9->9->9 + 9->9->9->9",
			args: args{CreateListNode([]int{9, 9, 9, 9, 9, 9, 9}), CreateListNode([]int{9, 9, 9, 9})},
			want: CreateListNode([]int{8, 9, 9, 9, 0, 0, 0, 1}),
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := addTwoNumbers(tt.args.l1, tt.args.l2); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("addTwoNumbers() = %v, want %v", got, tt.want)
			}
		})
	}
}
