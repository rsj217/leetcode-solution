package g_5_longest_palindromic_substring

func longestPalindrome(s string) string {
	ans := ""
	var s1, s2, ss string

	for i := 0; i < len(s); i++ {
		s1 = _longestSubPalindrome(i, i, s)
		s2 = _longestSubPalindrome(i, i+1, s)

		if len(s1) <= len(s2) {
			ss = s2
		} else {
			ss = s1
		}
		if len(ans) < len(ss) {
			ans = ss
		}
	}
	return ans
}

func _longestSubPalindrome(l, r int, s string) string {
	for 0 <= l && r < len(s) && s[l] == s[r] {
		l -= 1
		r += 1
	}
	return s[l+1 : r]
}
