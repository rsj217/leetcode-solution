package g_33_search_in_rotated_sorted_array

func search(nums []int, target int) int {
	lo, hi := 0, len(nums)
	for lo < hi {
		mid := lo + (hi-lo)/2
		if nums[mid] == target {
			return mid
		} else if nums[lo] <= nums[mid] {
			if nums[lo] <= target && target < nums[mid] {
				hi = mid
			} else {
				lo = mid + 1
			}
		} else { // nums[mid] < nums[lo]
			if nums[mid] < target && target <= nums[hi-1] {
				lo = mid + 1
			} else {
				hi = mid
			}
		}
	}
	return -1
}
