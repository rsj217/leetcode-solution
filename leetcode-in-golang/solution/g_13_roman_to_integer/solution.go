package g_13_roman_to_integer

func romanToInt(s string) int {
	ans := 0
	i := 0

	t := map[byte]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	for i < len(s) {
		if i+1 < len(s) && t[s[i]] < t[s[i+1]] {
			ans += t[s[i+1]] - t[s[i]]
			i += 2
		} else {
			ans += t[s[i]]
			i++
		}
	}
	return ans
}
