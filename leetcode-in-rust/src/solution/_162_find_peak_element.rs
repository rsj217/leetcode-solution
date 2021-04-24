pub struct Solution {}


impl Solution {
    pub fn find_peak_element(nums: Vec<i32>) -> i32 {
        let (mut lo, mut hi) = (0, nums.len());
        while 1 < hi - lo{
            let mid = lo + (hi - lo) / 2;
            if nums[mid-1] > nums[mid]{
                hi = mid
            } else {
                lo = mid
            }
        }
        lo as i32
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solution() {
        let test_case = vec![
            (vec![1, 2, 1, 3, 5, 6, 4], vec![1, 5]),
            (vec![1, 2, 3, 1], vec![2]),
            (vec![1, 2, 3], vec![2]),
            (vec![3, 2, 1], vec![0]),
            (vec![3], vec![0]),
            (vec![3, 2], vec![0]),
            (vec![2, 3], vec![1]),
        ];
        for (nums, answer) in test_case {
            let ans = Solution::find_peak_element(nums);
            assert_eq!(true, answer.contains(&ans));
        }
    }
}
