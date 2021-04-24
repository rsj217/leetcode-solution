package g_15_3sum

import "sort"

func threeSum(nums []int) [][]int {
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})
	ans := make([][]int, 0, 10)
	for i := 0; i < len(nums)-2; i++ {
		if i > 0 && nums[i-1] == nums[i] {
			continue
		}

		l, r := i+1, len(nums)-1
		for l < r {
			d := nums[i] + nums[l] + nums[r]
			if d == 0 {
				ans = append(ret, []int{nums[i], nums[l], nums[r]})

				for l < r && nums[l] == nums[l+1] {
					l++
				}
				for l < r && nums[r-1] == nums[r] {
					r--
				}
				l++
				r--

			} else if d < 0 {
				l++
			} else {
				r--
			}
		}
	}
	return ans
}
