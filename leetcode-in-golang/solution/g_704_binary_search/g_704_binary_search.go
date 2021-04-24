package g_704_binary_search

func search(nums []int, target int) int {
	lo, hi := 0, len(nums)
	for lo < hi {
		mid := lo + (hi-lo)/2
		if nums[mid] < target {
			lo = mid + 1
		} else if target < nums[mid] {
			hi = mid
		} else {
			return mid
		}
	}
	return -1
}
