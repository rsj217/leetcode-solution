
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l, r = 0, 0
        count = dict()
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            while count[s[r]] > 1:
                count[s[l]] = count[s[l]] - 1
                l += 1
            max_len = max(max_len, r-l+1)
            r += 1
        return max_len

