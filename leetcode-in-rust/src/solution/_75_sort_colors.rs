pub struct Solution {}

impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        let (mut l, mut i, mut r) = (0, 0, nums.len() - 1);
        while i <= r {
            match nums[i] {
                0 => {
                    nums.swap(l, i);
                    l += 1;
                    i += 1;
                }
                1 => i += 1,
                _ => {
                    nums.swap(r, i);
                    if r == 0 {
                        break;
                    }
                    r -= 1;
                }
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solution() {
        let test_case: Vec<(Vec<i32>, Vec<i32>)> = vec![
            (vec![2, 0, 2, 1, 1, 0], vec![0, 0, 1, 1, 2, 2]),
            (vec![2, 0, 1], vec![0, 1, 2]),
            (vec![0, 1, 0], vec![0, 0, 1]),
            (vec![0], vec![0]),
            (vec![1], vec![1]),
            (vec![2], vec![2]),
        ];
        for (mut nums, answer) in test_case {
            Solution::sort_colors(nums.as_mut());
            assert_eq!(nums, answer);
        }
    }
}
