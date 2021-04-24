package g_154_find_minimum_in_rotated_array_ii

func findMin(nums []int) int {
	l, r := 0, len(nums)-1
	for l < r {
		mid := l + (r-l)/2
		if nums[mid] == nums[r] {
			r--
		} else if nums[mid] < nums[r] {
			r = mid
		} else { // nums[r] < nums[mid]
			l = mid + 1
		}
	}
	return nums[l]
}
