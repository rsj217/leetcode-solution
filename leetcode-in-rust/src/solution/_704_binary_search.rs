pub struct Solution {}

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let (mut lo, mut hi) = (0, nums.len());
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if target < nums[mid] {
                hi = mid;
            } else if nums[mid] < target {
                lo = mid + 1;
            } else { // target == nums[mid]
                return mid as i32;
            }
        }
        -1
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solution() {
        let test_case = vec![
            (vec![-1, 0, 3, 5, 9, 12], 9, 4),
            (vec![-1, 0, 3, 5, 9, 12], 2, -1),
        ];
        for (nums, target, answer) in test_case {
            let ans = Solution::search(nums, target);
            assert_eq!(answer, ans);
        }
    }
}
