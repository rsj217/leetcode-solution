package datastruct

import (
	"reflect"
	"testing"
)

func TestListNode_String(t *testing.T) {
	type fields struct {
		Val  int
		Next *ListNode
	}
	tests := []struct {
		name   string
		fields *fields
		want   string
	}{
		{
			name:   "list print",
			fields: &fields{3, &ListNode{5, &ListNode{6, &ListNode{2, nil}}}},
			want:   "3->5->6->2->",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			ln := &ListNode{
				Val:  tt.fields.Val,
				Next: tt.fields.Next,
			}
			if got := ln.String(); got != tt.want {
				t.Errorf("String() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestListNode_ToSlice(t *testing.T) {
	type fields struct {
		Val  int
		Next *ListNode
	}
	tests := []struct {
		name   string
		fields *fields
		want   []int
	}{
		{
			name:   "to slice",
			fields: &fields{3, &ListNode{5, &ListNode{6, &ListNode{2, nil}}}},
			want:   []int{3, 5, 6, 2},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			ln := &ListNode{
				Val:  tt.fields.Val,
				Next: tt.fields.Next,
			}
			if got := ln.ToSlice(); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("ToSlice() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_CreateListNode(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want *ListNode
	}{
		{
			name: "[3, 5, 6, 2]",
			args: args{[]int{3, 5, 6, 2}},
			want: &ListNode{3, &ListNode{5, &ListNode{6, &ListNode{2, nil}}}},
		},
		{
			name: "[]",
			args: args{[]int{}},
			want: nil,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := CreateListNode(tt.args.nums); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("createListNode() = %v, want %v", got, tt.want)
			}
		})
	}
}
