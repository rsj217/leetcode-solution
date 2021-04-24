fn partition<T: PartialOrd + Copy>(nums: &mut Vec<T>, lo: usize, hi: usize) -> usize {
    let mut j = lo;
    for i in lo..hi {
        if nums[i] <= nums[lo] {
            nums.swap(j, i);
            j += 1;
        }
    }
    nums.swap(lo, j - 1);
    j - 1
}


pub fn quick_sort<T: PartialOrd + Copy>(nums: &mut Vec<T>) {
    fn dfs<T: PartialOrd + Copy>(nums: &mut Vec<T>, lo: usize, hi: usize) {
        if hi - lo <= 1 {
            return;
        }
        let p = partition(nums, lo, hi);
        dfs(nums, lo, p);
        dfs(nums, p + 1, hi);
    }
    dfs(nums, 0, nums.len());
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
            quick_sort(&mut nums);
            assert_eq!(is_sorted(nums), true);
        }
    }
}
