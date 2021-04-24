pub struct Solution {}

impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut r = 0;
        for &i in nums.iter() {
            r ^= i;
        }
        r
    }
}


#[cfg(test)]
mod tests {
    use super::*;


    #[test]
    fn test_solution() {
        let test_case = vec![
            (vec![2, 2, 1], 1),
            (vec![4, 1, 2, 1, 2], 4),
        ];
        for (nums, answer) in test_case {
            let ans = Solution::single_number(nums);
            assert_eq!(answer, ans);
        }
    }
}