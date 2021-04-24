pub struct Solution;

impl Solution {
    pub fn reverse(x: i32) -> i32 {
        Solution::_reverse(x).unwrap_or_default()
    }

    fn _reverse(mut x: i32) -> Option<i32> {
        let mut ans = 0i32;
        while x != 0 {
            let pop = x % 10;
            ans = ans.checked_mul(10)?.checked_add(pop)?;
            x /= 10;
        }
        Some(ans)
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solution() {
        let test_case = vec![
            (123, 321),
            (0, 0),
            (-123, -321),
            (2147483647, 0),
            (1463847412, 2147483641),
            (1463847413, 0),
            (1534236469, 0)
        ];

        for (x, answer) in test_case {
            let ans = Solution::reverse(x);
            assert_eq!(answer, ans);
        }
    }
}
