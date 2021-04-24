package main

import "fmt"

func main() {
	a := []int{1, 2, 3}
	n := make([]int, 3, 3)
	fmt.Println(a, n)

	copy(n, a)
	fmt.Println(a, n)
}
