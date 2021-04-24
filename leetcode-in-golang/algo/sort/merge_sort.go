package sort

func mergeLeftRight(nums []int, lo, mid, hi int) {
	tmpNums := make([]int, 0, hi-lo)
	for i := lo; i < hi; i++ {
		tmpNums = append(tmpNums, nums[i])
	}
	lsize, rsize := mid-lo, hi-lo
	l, r := lo-lo, mid-lo

	for i := lo; i < hi; i++ {
		if l < lsize && r < rsize {
			if tmpNums[l] <= tmpNums[r] {
				nums[i] = tmpNums[l]
				l += 1
			} else {
				nums[i] = tmpNums[r]
				r += 1
			}
		} else {
			if l < lsize {
				nums[i] = tmpNums[l]
				l += 1
			} else { // r < rsize {
				nums[i] = tmpNums[r]
				r += 1
			}
		}
	}
}

func mergeSort(nums []int, lo, hi int) {
	if hi-lo <= 1 {
		return
	}
	mid := lo + (hi-lo)/2
	mergeSort(nums, lo, mid)
	mergeSort(nums, mid, hi)
	mergeLeftRight(nums, lo, mid, hi)
}

func MergeSort(nums []int) {
	mergeSort(nums, 0, len(nums))
}
