pub struct Solution {}

impl Solution {
    pub fn int_to_roman(num: i32) -> String {
        let mut num = num;
        let nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
        let letter = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
        let mut ans = String::new();
        for (i, &item) in nums.iter().enumerate() {
            while num >= item {
                num -= item;
                ans.push_str(letter[i]);
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
            (3, "III"),
            (4, "IV"),
            (9, "IX"),
            (58, "LVIII"),
            (1994, "MCMXCIV"),
        ];
        for (num, anwser) in test_case {
            let ans = Solution::int_to_roman(num);
            assert_eq!(ans, anwser);
        }
    }
}
