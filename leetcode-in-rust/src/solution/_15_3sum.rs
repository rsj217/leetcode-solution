pub struct Solution{}

impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut ans = vec![];
        if nums.len() <= 2{
            return ans;
        }
        let mut nums = nums;
        nums.sort();
        for i in 0..nums.len()-2 {
            if i > 0 && nums[i - 1] == nums[i] {
                continue
            }

            let mut l = i+1;
            let mut r = nums.len() - 1;

            while l < r {
                let d = nums[i] + nums[l] + nums[r];
                if d == 0 {
                    ans.push(vec![nums[i], nums[l], nums[r]]);
                    while l < r && nums[l] == nums[l + 1] {
                        l += 1
                    }
                    while l < r && nums[r - 1] == nums[r] {
                        r -= 1
                    }
                    l += 1;
                    r -= 1;

                } else if d < 0 {
                    l += 1;
                } else {
                    r -= 1
                }
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
        let input = vec![
            vec![-1, 0, 1, 2, -1, -4],
            vec![1,2,-2,-1],
            vec![],
            vec![0],
            vec![0, 0],
            vec![0, 0, 0, 0],
            vec![-1, -1, 0, 1],
        ];
        let answer :Vec<Vec<Vec<i32>>>= vec![
            vec![vec![-1, -1, 2], vec![-1, 0, 1]],
            vec![],
            vec![],
            vec![],
            vec![],
            vec![vec![0, 0, 0]],
            vec![vec![-1, 0, 1]],
        ];
        for (i, item) in input.iter().enumerate(){
            let ans = Solution::three_sum(item.to_vec());
            assert_eq!(answer[i], ans);
        }
    }
}
