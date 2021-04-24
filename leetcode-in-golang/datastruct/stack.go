package datastruct

type StackInt []int

func NewStackInt() StackInt {
	return StackInt{}
}

func (s StackInt) Empty() bool {
	return len(s) == 0
}

func (s *StackInt) Push(e int) {
	*s = append(*s, e)
}

func (s *StackInt) Pop() (e int) {
	if !s.Empty() {
		e = (*s)[len(*s)-1]
		*s = (*s)[0 : len(*s)-1]
	}
	return
}

type StackString []string

func NewStackString() StackString {
	return StackString{}
}

func (s StackString) Empty() bool {
	return len(s) == 0
}

func (s *StackString) Push(e string) {
	*s = append(*s, e)
}

func (s *StackString) Pop() (e string) {
	if !s.Empty() {
		e = (*s)[len(*s)-1]
		*s = (*s)[0 : len(*s)-1]
	}
	return
}
