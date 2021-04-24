
pub struct Solution{}

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> bool {
        let (mut lo, mut hi) = (0, nums.len());
        while lo < hi{
            let mid = lo + (hi - lo) / 2;
            if nums[mid] == target{
                return true;
            } else if nums[lo] == nums[mid] {
                lo += 1;
            } else if nums[lo] < nums[mid]{
                if nums[lo] <= target && target < nums[mid] {
                    hi = mid;
                }else {
                    lo = mid + 1;
                }
            } else { // nums[mid] < nums[lo]
                if nums[mid] < target && target <= nums[hi-1]{
                    lo = mid + 1;
                }else {
                    hi = mid;
                }
            }
        }
        false
    }
}


#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_solution() {
        let test_case = vec![
            (vec![2, 5, 6, 0, 0, 1, 2], 0, true),
            (vec![2, 5, 6, 0, 0, 1, 2], 3, false),
            (vec![1, 0, 1, 1, 1], 0, true),
            (vec![1, 1, 1, 2, 1], 2, true),
            (vec![5, 1, 3], 3, true)
        ];

        for (nums, target, answer) in test_case{
            let ans = Solution::search(nums, target);
            assert_eq!(answer, ans);
        }
    }
}
