package g_81_search_in_rotated_sorted_array_ii

func searchII(nums []int, target int) bool {
	lo, hi := 0, len(nums)
	for lo < hi {
		mid := lo + (hi-lo)/2
		if nums[mid] == target {
			return true
		} else if nums[lo] == nums[mid] {
			lo++
		} else if nums[lo] < nums[mid] {
			if nums[lo] <= target && target < nums[mid] {
				hi = mid
			} else {
				lo = mid + 1
			}
		} else { // nums[mid] < nums[mid]
			if nums[mid] < target && target <= nums[hi-1] {
				lo = mid + 1
			} else {
				hi = mid
			}
		}
	}
	return false
}
