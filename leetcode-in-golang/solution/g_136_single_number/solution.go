package g_136_single_number

func singleNumber(nums []int) int {
	ans := 0
	for _, v := range nums {
		ans ^= v
	}
	return ans
}
