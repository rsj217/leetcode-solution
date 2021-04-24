pub struct Solution;

impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        let s = s.as_bytes();
        let mut ans = "";
        for (i, _) in s.iter().enumerate() {
            let s1 = Solution::_longest_palindrome(s, i, i);
            let s2 = Solution::_longest_palindrome(s, i, i + 1);
            let ss = if s1.len() < s2.len() { s2 } else { s1 };
            if ans.len() < ss.len() {
                ans = ss;
            }
        }
        ans.to_string()
    }

    fn _longest_palindrome(s: &[u8], l: usize, r: usize) -> &str {
        let (mut l, mut r) = (l, r);
        // 0 <= usize always true, It means 0 <= l always true
        while r < s.len() && s[l] == s[r] {
            if l == 0 {
                return std::str::from_utf8(&s[l..r + 1]).unwrap();
            }
            l -= 1;
            r += 1;
        }
        std::str::from_utf8(&s[l + 1..r]).unwrap()
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solution() {
        let test_case = vec![
            ("babad".to_string(), "bab"),
            ("cbbd".to_string(), "bb"),
            ("a".to_string(), "a"),
            ("".to_string(), ""),
            ("ab".to_string(), "a"),
            ("aa".to_string(), "aa"),
        ];
        for (item, answer) in test_case {
            let ans = Solution::longest_palindrome(item);
            assert_eq!(answer.to_string(), ans);
        }
    }
}
