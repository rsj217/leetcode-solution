pub struct Solution {}

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut max_profit = 0;
        let mut min_price = prices[0];
        for cur_price in prices {
            if cur_price < min_price {
                min_price = cur_price;
            } else if max_profit < cur_price - min_price {
                max_profit = cur_price - min_price
            }
        }
        max_profit
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solution() {
        let test_case = vec![
            (vec![7, 1, 5, 3, 6, 4], 5),
            (vec![7, 6, 4, 3, 1], 0),
            (vec![5], 0),
            (vec![4, 5], 1),
        ];
        for (nums, answer) in test_case {
            let ans = Solution::max_profit(nums);
            assert_eq!(ans, answer);
        }
    }
}
