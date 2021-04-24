pub fn insert_sort<T: PartialOrd + Copy>(nums: &mut Vec<T>) {
    for i in 0..nums.len() {
        let mut j = i;
        let curnum = nums[i];
        while 0 < j && curnum < nums[j - 1] {
            nums[j] = nums[j - 1];
            j -= 1;
        }
        nums[j] = curnum;
    }
}


// 1 , 2, 3

#[cfg(test)]
mod tests {
    use super::*;
    use crate::algo::sort::helper::is_sorted;

    #[test]
    fn test_is_sorted() {
        let test_case = vec![
            vec![0, 0, 0],
            vec![1, 2, 4, 5],
            vec![3, 3],
            vec![3, 1, 3],
            vec![3, 1, 0],
        ];

        for mut nums in test_case {
            insert_sort(&mut nums);
            assert_eq!(is_sorted(nums), true);
        }
    }
}
