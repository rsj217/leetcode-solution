package sort

func insertSort(nums []int, lo, hi int) {
	for i := lo; i < hi; i++ {
		curnum := nums[i]
		j := i
		for ; 0 < j && curnum < nums[j-1]; j-- {
			nums[j] = nums[j-1]
		}
		nums[j] = curnum
	}
}

func InsertSort(nums []int) {
	insertSort(nums, 0, len(nums))
}
