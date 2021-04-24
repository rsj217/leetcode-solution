pub fn is_sorted<T: PartialOrd + Copy>(nums: Vec<T>) -> bool {
    if nums.len() == 0 {
        return true;
    }
    for i in 0..nums.len() - 1 {
        if nums[i] > nums[i + 1] {
            return false;
        }
    }
    true
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_is_sorted() {
        let test_case = vec![
            (vec![], true),
            (vec![1, 2, 4], true),
            (vec![3, 3], true),
            (vec![3, 1, 3], false),
            (vec![3, 1, 0], false),
        ];

        for (nums, answer) in test_case {
            let ans = is_sorted(nums);
            assert_eq!(ans, answer);
        }
    }
}
