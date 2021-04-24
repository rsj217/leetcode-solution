pub struct Solution {}

impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        let (mut lo, mut hi) = (0, nums.len());
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if nums[mid] < target {
                lo = mid + 1
            } else {
                hi = mid
            }
        }
        hi as i32
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solution() {
        let test_case = vec![
            (vec![1, 3, 4, 6], 0, 0, ),
            (vec![1, 3, 4, 6], 2, 1, ),
            (vec![1, 3, 4, 6], 5, 3, ),
            (vec![1, 3, 4, 6], 7, 4, ),
            (vec![4, 5, 5, 5], 5, 1, ),
            (vec![5, 5, 5, 5], 5, 0, ),
        ];


        for (nums, target, answer) in test_case {
            let ans = Solution::search_insert(nums, target);
            assert_eq!(ans, answer);
        }
    }
}
