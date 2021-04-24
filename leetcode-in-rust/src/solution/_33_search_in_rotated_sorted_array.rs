pub struct Solution {}

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let (mut lo, mut hi) = (0, nums.len());

        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if nums[mid] == target {
                return mid as i32;
            } else if nums[lo] < nums[mid] {
                if nums[lo] <= target && target < nums[mid] {
                    hi = mid;
                } else {
                    lo = mid + 1;
                }
            } else { // nums[lo] > nums[mid]
                if nums[mid] < target && target < nums[lo] {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
        }
        -1
    }
}


#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_solution() {
        // 题意：nums 中的每个值都 独一无二
        let test_case: Vec<(Vec<i32>, i32, i32)> = vec![
            (vec![4, 5, 6, 7, 0, 1, 2], 0, 4),
            (vec![4, 5, 6, 7, 0, 1, 2], 3, -1),
            (vec![1], 0, -1),
            (vec![5], 1, -1),
            (vec![5], 5, 0),
            (vec![4, 5], 3, -1),
            (vec![4, 5], 4, 0),
            (vec![4, 5], 5, 1),
            (vec![4, 5], 6, -1),
            (vec![5, 4], 3, -1),
            (vec![5, 4], 4, 1),
            (vec![5, 4], 5, 0),
            (vec![6, 7, 1, 2, 3], 7, 1),
            (vec![5, 2, 3], 2, 1),
            (vec![6, 7, 0, 2, 3], 2, 3),
            (vec![6, 7, 0, 2, 3], 6, 0),
            (vec![6, 7, 0, 2, 3], 6, 0),
        ];

        for (item,target,answer) in test_case {
            let ans = Solution::search(item.to_vec(), target);
            assert_eq!(ans, answer);
        }
    }
}
