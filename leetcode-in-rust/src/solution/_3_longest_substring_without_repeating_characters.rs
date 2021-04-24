use std::cmp::max;

pub struct Solution;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut max_len = 0;
        let mut l = 0;
        let mut count = [0; 255];
        let bytes = s.as_bytes();
        for (r, &v) in bytes.iter().enumerate() {
            count[v as usize] += 1;
            while count[v as usize] > 1 {
                count[bytes[l] as usize] -= 1;
                l += 1;
            }
            max_len = max(max_len, r - l + 1)
        }
        max_len as i32
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solution() {
        let test_case = vec![
            ("abcabcbb".to_string(), 3),
            ("bbbbb".to_string(), 1),
            ("pwwkew".to_string(), 3),
            ("".to_string(), 0),
        ];
        for (s, answer) in test_case {
            let ans = Solution::length_of_longest_substring(s);
            assert_eq!(ans, answer);
        }
    }
}
