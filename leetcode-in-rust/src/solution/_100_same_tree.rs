use crate::datastruct::treenode::TreeNode;
use std::rc::Rc;
use std::cell::RefCell;

pub struct Solution {}

impl Solution {
    pub fn is_same_tree(p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn dfs(p: &Option<Rc<RefCell<TreeNode>>>, q: &Option<Rc<RefCell<TreeNode>>>) -> bool {
            match (p, q) {
                (Some(p), Some(q)) if p == q => {
                    dfs(&p.borrow().left, &q.borrow().left) && dfs(&p.borrow().right, &q.borrow().right)
                },
                (None, None) => true,
                _ => false,
            }
        }
        dfs(&p, &q)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solution() {
        let test_case = vec![
            (
                vec![Some(3), Some(9), Some(20), None, None, Some(15), Some(7)],
                vec![Some(3), Some(9), Some(20), None, None, Some(15), Some(7)],
                true,
            ),
        ];
        for (a, b, answer) in test_case {
            let p = TreeNode::create(a);
            let q = TreeNode::create(b);
            let ans = Solution::is_same_tree(p, q);
            assert_eq!(ans, answer);
        }
    }
}
