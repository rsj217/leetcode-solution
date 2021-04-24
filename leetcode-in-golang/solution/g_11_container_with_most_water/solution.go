package g_11_container_with_most_water

func maxArea(height []int) int {
	ans := 0
	area := 0
	l, r := 0, len(height)-1
	for l < r {
		if height[l] < height[r] {
			area = height[l] * (r - l)
			l++
		} else {
			area = height[r] * (r - l)
			r--
		}
		if ans < area {
			ans = area
		}
	}
	return ans
}
