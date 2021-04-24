package sort

func partial(nums []int, lo, hi int) int {
	j := lo
	for i := lo; i < hi; i++ {
		if nums[i] <= nums[lo] {
			nums[j], nums[i] = nums[i], nums[j]
			j++
		}
	}
	nums[lo], nums[j-1] = nums[j-1], nums[lo]
	return j - 1
}

func quickSort(nums []int, lo, hi int) {
	if hi-lo <= 1 {
		//insertSort(nums, lo, hi)
		return
	}
	p := partial(nums, lo, hi)
	quickSort(nums, lo, p)
	quickSort(nums, p+1, hi)
}

func partition3way(nums []int, lo, hi int) (int, int) {
	midNum := nums[lo]
	j, i, k := lo, lo, hi-1
	for i <= k {
		switch {

		case nums[i] < midNum:
			nums[j], nums[i] = nums[i], nums[j]
			j++
			i++
		case midNum < nums[i]:
			nums[i], nums[k] = nums[k], nums[i]
			k--
		case midNum == nums[i]:
			i++
		}
	}
	return j, k
}

func quick3WaySort(nums []int, lo, hi int) {
	if hi-lo <= 1 {
		return
	}
	j, k := partition3way(nums, lo, hi)
	quick3WaySort(nums, lo, j)
	quick3WaySort(nums, k+1, hi)
}

func Quick3WaySort(nums []int) {
	quick3WaySort(nums, 0, len(nums))
}

func QuickSort(nums []int) {
	quickSort(nums, 0, len(nums))
}
