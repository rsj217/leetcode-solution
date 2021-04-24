fn merge_left_right<T: PartialOrd + Copy>(nums: &mut Vec<T>, lo: usize, mid: usize, hi: usize) {
    let mut tmp_nums = Vec::new();
    for i in lo..hi {
        tmp_nums.push(nums[i])
    }

    let (lsize, rsize) = (mid - lo, hi - lo);
    let (mut l, mut r) = (lo - lo, mid - lo);
    for i in lo..hi {
        if l < lsize && r < rsize {
            if tmp_nums[l] <= tmp_nums[r] {
                nums[i] = tmp_nums[l];
                l += 1;
            } else {
                nums[i] = tmp_nums[r];
                r += 1;
            }
        } else {
            if l < lsize {
                nums[i] = tmp_nums[l];
                l += 1;
            } else { // r < rsize
                nums[i] = tmp_nums[r];
                r += 1;
            }
        }
    }
}


pub fn merge_sort<T: PartialOrd + Copy>(nums: &mut Vec<T>) {
    fn dfs<T: PartialOrd + Copy>(nums: &mut Vec<T>, lo: usize, hi: usize) {
        if hi - lo <= 1 {
            return;
        }

        let mid = lo + (hi - lo) / 2;
        dfs(nums, lo, mid);
        dfs(nums, mid, hi);
        merge_left_right(nums, lo, mid, hi);
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
            merge_sort(&mut nums);
            assert_eq!(is_sorted(nums), true);
        }
    }
}
