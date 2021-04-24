package g_162_find_peak_element

func find_peak_element(nums []int) int {
	lo, hi := 0, len(nums)
	for 1 < hi-lo {
		mid := lo + (hi-lo)/2
		if nums[mid-1] > nums[mid] {
			hi = mid
		} else {
			lo = mid
		}
	}
	return lo
}
