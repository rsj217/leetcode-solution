package util

import (
	"math/rand"
	"time"
)

func init() {
	rand.Seed(time.Now().UnixNano())
}

func ContainInt(nums []int, x int) bool {
	for _, v := range nums {
		if v == x {
			return true
		}
	}
	return false
}

func IsSorted(nums []int) bool {
	for i := 0; i < len(nums)-1; i++ {
		if nums[i] > nums[i+1] {
			return false
		}
	}
	return true
}

func RandomInt(l, r int) int {
	return l + rand.Intn(r-l)
}

func RandomNums(size, l, r int) []int {
	nums := make([]int, size)
	for i, _ := range nums {
		num := RandomInt(l, r)
		nums[i] = num
	}
	return nums
}

func RandomNearlyOrderNums(size, swap int) []int {
	nums := make([]int, size)
	for i, _ := range nums {
		nums[i] = i
	}
	for i := 0; i < swap; i++ {
		l := RandomInt(0, size)
		r := RandomInt(0, size)
		nums[l], nums[r] = nums[r], nums[l]
	}
	return nums
}
