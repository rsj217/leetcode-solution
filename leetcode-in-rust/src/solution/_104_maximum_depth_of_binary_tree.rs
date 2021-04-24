use crate::datastruct::treenode::TreeNode;

pub struct Solution {}

use std::rc::Rc;
use std::cell::RefCell;
use std::cmp::max;

impl Solution {
    pub fn max_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
            // if let Some(node) = node {
            //     let node = node.borrow();
            //     return 1 + max(
            //         dfs(&node.left),
            //         dfs(&node.right),
            //     );
            // }
            // 0
            //
            match node {
                Some(node) => {
                    let node = node.borrow();
                    1 + max(dfs(&node.left), dfs(&node.right))
                }
                None => 0,
            }
        }
        dfs(&root)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solution() {
        let test_case = vec![
            (vec![Some(3), Some(9), Some(20), None, None, Some(15), Some(7)], 3),
        ];
        for (nums, answer) in test_case {
            let root = TreeNode::create(nums);
            let ans = Solution::max_depth(root);
            assert_eq!(ans, answer)
        }
    }
}
