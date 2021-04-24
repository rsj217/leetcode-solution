pub struct Solution {}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut t = std::collections::HashMap::with_capacity(nums.len());
        for (index, &item) in nums.iter().enumerate() {
            let index = index as i32;
            match t.get(&(target - item)) {
                Some(&i) => return vec![i, index as i32],
                None => t.insert(item, index),
            };
        }
        return vec![];
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solution(){
        let test_case = vec![
            (vec![2, 7, 1, 5], 9, vec![0, 1]),
            (vec![3, 2, 4], 6, vec![1, 2]),
            (vec![3, 3], 6, vec![0, 1]),
        ];

        for (nums, target, answer) in test_case{
            let ans = Solution::two_sum(nums, target);
            assert_eq!(ans, answer);
        }
    }
}
