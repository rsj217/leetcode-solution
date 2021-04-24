package g_7_reverse_integer

import "math"

func reverse(x int) int {
	ans := 0
	MaxInt32 := math.MaxInt32
	MinInt32 := -math.MaxInt32 - 1

	for x != 0 {
		pop := x % 10

		if ans > MaxInt32/10 || (ans == MaxInt32/10 && pop > 7) {
			return 0
		}
		if ans < MinInt32/10 || (ans == MinInt32/10 && pop < -8) {
			return 0
		}
		ans = ans*10 + pop
		x /= 10
	}
	return ans
}
