pub struct Solution {}

impl Solution {
    fn roman_int_map(c: char) -> i32 {
        match c {
            'I' => 1,
            'V' => 5,
            'X' => 10,
            'L' => 50,
            'C' => 100,
            'D' => 500,
            'M' => 1000,
            _ => 0
        }
    }
    pub fn roman_to_int(s: String) -> i32 {
        let mut ans = 0;
        let s_bytes = s.as_bytes();
        let mut i = 0;
        while i < s_bytes.len() {
            if i + 1 < s_bytes.len() && Solution::roman_int_map(s_bytes[i] as char) < Solution::roman_int_map(s_bytes[i + 1] as char) {
                ans += Solution::roman_int_map(s_bytes[i + 1] as char) - Solution::roman_int_map(s_bytes[i] as char);
                i += 2;
            } else {
                ans += Solution::roman_int_map(s_bytes[i] as char);
                i += 1;
            }
        }
        ans
    }
}


#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_solution() {
        let test_case = vec![
            ("III".to_string(), 3),
            ("IV".to_string(), 4),
            ("IX".to_string(), 9),
            ("LVIII".to_string(), 58),
            ("MCMXCIV".to_string(), 1994),
        ];

        for (s, answer) in test_case {
            let ans = Solution::roman_to_int(s);
            assert_eq!(ans, answer);
        }
    }
}
