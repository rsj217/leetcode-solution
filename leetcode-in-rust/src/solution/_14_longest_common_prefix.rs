pub struct Solution {}

impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        if strs.len() <= 0 {
            return "".to_string();
        }

        let mut min_str = &strs[0];
        for item in strs.iter() {
            if item.len() < min_str.len() {
                min_str = item;
            }
        }

        let mut hi = 0;
        for (i, &item) in min_str.as_bytes().iter().enumerate() {
            for w in strs.iter() {
                if item != w.as_bytes()[i] {
                    return min_str[0..i].to_string();
                }
            }
            hi += 1;
        }
        min_str[0..hi].to_string()
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solution() {
        let test_case = vec![
            (vec!["flower".to_string(), "flow".to_string(), "flight".to_string()], "fl".to_string()),
            (vec!["dog".to_string(), "racecar".to_string(), "car".to_string()], "".to_string()),
            (vec!["".to_string(), "".to_string(), "".to_string()], "".to_string()),
            (vec!["".to_string(), "qwe".to_string()], "".to_string()),
            (vec!["qwe".to_string(), "".to_string()], "".to_string()),
            (vec!["abc".to_string(), "abc".to_string()], "abc".to_string()),
            (vec!["a".to_string()], "a".to_string()),
            (vec!["".to_string()], "".to_string()),
            (vec![], "".to_string()),
        ];
        for (strs, answer) in test_case {
            let ans = Solution::longest_common_prefix(strs);
            assert_eq!(ans, answer);
        }
    }
}
