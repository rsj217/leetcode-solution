pub struct Solution {}

impl Solution {
    pub fn square(mid:i32) -> Option<i32>{
        let mid = mid.checked_mul(mid)?;
        Some(mid)
    }
    pub fn my_sqrt(x: i32) -> i32 {
        let (mut l, mut r) = (0, x);
        let mut ans = 0;
        while l <= r {
            let mid = l + (r - l) / 2;
            let mid_square = Solution::square(mid);
            if mid_square.is_some() && mid_square.le(&Some(x)) {
                ans = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        ans
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solution() {
        let test_case = vec![
            (0, 0),
            (1, 1),
            (2, 1),
            (4, 2),
            (8, 2),
            (15, 3),
            (2147395599, 46339),
            (2147483647, 46340),
        ];

        for (x, answer) in test_case {
            let ans = Solution::my_sqrt(x);
            assert_eq!(ans, answer);
        }
    }
}
