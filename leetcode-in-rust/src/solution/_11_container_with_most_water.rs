pub struct Solution {}

impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let (mut l, mut r) = (0usize, height.len() - 1);
        let mut ans = 0;
        let mut area;
        while l < r {
            if height[l] < height[r] {
                area = height[l] * (r - l) as i32;
                l += 1
            } else {
                area = height[r] * (r - l) as i32;
                r -= 1
            }
            if ans < area {
                ans = area
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
            (vec![1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
            (vec![1, 1], 1),
            (vec![4, 3, 2, 1, 4], 16),
            (vec![1, 2, 1], 2)
        ];
        for (nums, answer) in test_case {
            let ans = Solution::max_area(nums);

            assert_eq!(ans, answer);
        }
    }
}
