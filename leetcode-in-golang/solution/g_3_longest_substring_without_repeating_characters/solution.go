package g_3_longest_substring_without_repeating_characters

func lengthOfLongestSubstring(s string) int {
	count := make(map[byte]int)
	maxLen := 0
	l, r := 0, 0
	for r < len(s) {
		count[s[r]] += 1
		for count[s[r]] > 1 {
			count[s[l]] -= 1
			l += 1
		}
		len_ := r - l + 1
		if maxLen < len_ {
			maxLen = len_
		}
		r += 1
	}
	return maxLen
}
