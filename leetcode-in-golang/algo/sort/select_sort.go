package sort

func selectSort(nums []int, lo, hi int) {
	for i := lo; i < hi; i++ {
		minIndex := i
		for j := i; j < len(nums); j++ {
			if nums[j] < nums[minIndex] {
				minIndex = j
			}
		}
		nums[i], nums[minIndex] = nums[minIndex], nums[i]
	}
}

func SelectSort(nums []int) {
	selectSort(nums, 0, len(nums))
}
