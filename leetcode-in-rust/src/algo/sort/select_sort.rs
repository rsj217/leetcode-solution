pub fn select_sort<T: PartialOrd + Copy>(nums: &mut Vec<T>) {
    for i in 0..nums.len(){
        let mut min_index = i;
        for j in i..nums.len(){
            if nums[j] < nums[min_index]{
                min_index = j;
            }
        }
        nums.swap(i, min_index);
    }
}


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
            select_sort(&mut nums);
            assert_eq!(is_sorted(nums), true);
        }
    }
}
