package g_75_sort_colors

func sortColors(nums []int) {
	l, i, r := 0, 0, len(nums)-1
	for i <= r {
		switch nums[i] {
		case 0:
			nums[l], nums[i] = nums[i], nums[l]
			l++
			i++
		case 1:
			i++
		case 2:
			nums[i], nums[r] = nums[r], nums[i]
			r--
		}
	}
}
