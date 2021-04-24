package g_12_integer_to_roman

func intToRoman(num int) string {
	value := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
	letter := []string{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}
	ans := ""
	for i, v := range value {
		for num >= v {
			num -= v
			ans += letter[i]
		}
	}
	return ans
}
