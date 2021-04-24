package g_1_two_sum

func twoSum(nums []int, target int) []int {
	t := make(map[int]int)
	for index, v := range nums {
		if preIndex, ok := t[target-v]; ok {
			return []int{preIndex, index}
		}
		t[v] = index
	}
	return []int{}
}
