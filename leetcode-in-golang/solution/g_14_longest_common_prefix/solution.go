package g_14_longest_common_prefix

func longestCommonPrefix(strs []string) string {
	if len(strs) <= 0 {
		return ""
	}
	hi := 0
	minStr := strs[0]
	for _, str := range strs {
		if len(str) < len(minStr) {
			hi = len(str)
		} else {
			hi = len(minStr)
		}
		i := 0
		for i < hi && str[i] == minStr[i] {
			i += 1
		}
		minStr = str[0:i]
	}
	return minStr
}

func longestCommonPrefix1(strs []string) string {
	if len(strs) <= 0 {
		return ""
	}
	minStr := strs[0]
	for _, s := range strs {
		if len(s) < len(minStr) {
			minStr = s
		}
	}
	hi := 0
	for i := 0; i < len(minStr); i++ {
		for _, s := range strs {
			if minStr[i] != s[i] {
				return minStr[0:i]
			}
		}
		hi += 1
	}
	return minStr[0:hi]
}
