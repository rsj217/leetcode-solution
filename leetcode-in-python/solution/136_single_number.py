from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        t = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        ans = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and t[s[i]] < t[s[i+1]]:
                ans += t[s[i+1]] - t[s[i]]
                i += 2
            else:
                ans += t[s[i]]
                i += 1
        return ans