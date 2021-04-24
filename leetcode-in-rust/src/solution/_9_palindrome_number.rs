pub struct Solution;

impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let mut n = x;
        let mut r = 0;
        while n > 0 {
            r = r * 10 + n % 10;
            n /= 10;
        }
        x == r
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solution() {
        let test_case = vec![
            (123, false),
            (121, true),
            (-121, false),
            (-0, true),
            (0, true),
            (1221, true),
            (12321, true),
        ];

        for (x, answer) in test_case{
            let ans = Solution::is_palindrome(x);
            assert_eq!(ans, answer);
        }
    }
}
