use crate::datastruct::treenode::TreeNode;
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;
use std::option::Option::Some;

pub struct Solution {}

impl Solution {
    pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        if root.is_none() {
            return vec![];
        }
        let mut ans = vec![];
        let mut queue = VecDeque::new();
        queue.push_back(root);
        while !queue.is_empty() {
            let size = queue.len();
            let mut level = vec![];
            for _i in 0..size {
                if let Some(ref node) = queue.pop_front().flatten() {
                    let node = node.borrow();

                    level.push(node.val);

                    if let Some(ref left) = node.left {
                        queue.push_back(Some(Rc::clone(left)))
                    }
                    if let Some(ref right) = node.right {
                        queue.push_back(Some(Rc::clone(right)))
                    }
                }
            }
            ans.push(level);
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
            (vec![Some(3), Some(9), Some(20), None, None, Some(15), Some(7)], vec![
                vec![3],
                vec![9, 20],
                vec![15, 7]
            ]),
        ];
        for (nums, answer) in test_case {
            let root = TreeNode::create(nums);
            let ans = Solution::level_order(root);
            assert_eq!(ans, answer);
        }
    }
}
