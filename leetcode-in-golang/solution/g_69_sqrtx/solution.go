package g_69_sqrtx

func mySqrt(x int) int {
	lo, hi := 0, x+1
	ans := 0
	for lo < hi {
		mid := lo + (hi-lo)/2
		if mid*mid <= x {
			ans = mid
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	return ans
}
