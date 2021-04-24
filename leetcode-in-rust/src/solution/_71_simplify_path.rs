pub struct Solution {}


impl Solution {
    pub fn simplify_path(path: String) -> String {
        let strings: Vec<&str> = path.as_str().split("/").collect();
        let mut stack: Vec<&str> = vec![];
        for i in strings {
            if i == "." || i == "" {
                continue;
            }
            if i == ".." {
                if !stack.is_empty() {
                    stack.pop();
                }
            } else {
                stack.push(i);
            }
        }
        format!("/{}", stack.join("/"))
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solution() {
        let test_case = vec![
            ("/home/", "/home"),
            ("/../", "/"),
            ("/", "/"),
            ("/.", "/"),
            ("/.a", "/.a"),
            ("/..a", "/..a"),
            ("/home//foo/", "/home/foo"),
            ("/a/./b/../../c/", "/c"),
            ("/a/../../b/../c//.//", "/c")
        ];
        for (nums, answer) in test_case {
            let ans = Solution::simplify_path(nums.to_string());
            assert_eq!(ans, answer);
        }
    }
}
