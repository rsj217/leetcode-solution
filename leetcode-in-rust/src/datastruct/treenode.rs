use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;
use std::cmp::max;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
    pub fn get_height(root: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(root: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
            // match root {
            //     None => -1,
            //     Some(node) => {
            //         let node = node.borrow();
            //         1 + max(dfs(&node.left), dfs(&node.right))
            //     }
            // }
            if let Some(node) = root {
                let node = node.borrow();
                1 + max(dfs(&node.left), dfs(&node.right))
            } else {
                -1
            }
        }
        dfs(&root)
    }

    pub fn create(nums: Vec<Option<i32>>) -> Option<Rc<RefCell<Self>>> {
        if nums.is_empty() {
            return None;
        }
        let size = nums.len();
        let mut index = 0;
        let root = Rc::new(RefCell::new(Self::new(nums[0].unwrap())));
        let mut queue = VecDeque::new();
        queue.push_back(Rc::clone(&root));
        while !queue.is_empty() {
            let queue_size = queue.len();
            for _i in 0..queue_size {
                index += 1;
                if let Some(node) = queue.pop_front() {
                    let mut node = node.borrow_mut();
                    if 2 * index - 1 < size && nums[2 * index - 1].is_some() {
                        node.left = Some(Rc::new(RefCell::new(Self::new(nums[2 * index - 1].unwrap()))));
                        queue.push_back(Rc::clone(node.left.as_ref().unwrap()));
                    }

                    if 2 * index < size && nums[2 * index].is_some() {
                        node.right = Some(Rc::new(RefCell::new(Self::new(nums[2 * index].unwrap()))));
                        queue.push_back(Rc::clone(node.right.as_ref().unwrap()));
                    }
                }
            }
        }
        Some(root)
    }
}

pub fn print_tree(root: Option<Rc<RefCell<TreeNode>>>, height: u32, width: &str) -> String {
    if root.is_none() {
        return "".to_string();
    }

    let mut deep = 0_u32;
    let mut levels = vec![];

    let mut queue = VecDeque::new();
    queue.push_back((root, 1));

    while !queue.is_empty() {
        let mut pre_index = 0;
        let mut level = vec![];

        let step = 2_u32.pow(height - deep + 1);
        let start = 2_u32.pow(height - deep) - 1;

        deep += 1;

        let size = queue.len();
        for index in 0..size {
            if let Some((Some(node), seq)) = queue.pop_front() {
                let node = node.borrow();

                let arr_index = start + (seq - 1) * step;
                let space = if index == 0 {
                    width.repeat(arr_index as usize)
                } else {
                    width.repeat((arr_index - pre_index - 1) as usize)
                };
                level.push(format!("{}{}", space, node.val));
                if index == size - 1 {
                    level.push("\n\n".to_string());
                }
                if let Some(ref left) = node.left {
                    queue.push_back((Some(Rc::clone(left)), 2 * seq - 1))
                }
                if let Some(ref right) = node.right {
                    queue.push_back((Some(Rc::clone(right)), 2 * seq))
                }
                pre_index = arr_index;
            }
        }
        levels.push(level.concat());
    }
    levels.concat()
}

pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) {
    let mut queue = VecDeque::new();
    queue.push_back(root);
    while !queue.is_empty() {
        let size = queue.len();
        for _i in 0..size {
            if let Some(node) = queue.pop_front().flatten() {
                let node = node.borrow();
                println!("{}", node.val);
                if let Some(ref left) = node.left {
                    queue.push_back(Some(Rc::clone(left)))
                }
                if let Some(ref right) = node.right {
                    queue.push_back(Some(Rc::clone(right)))
                }
                // if node.left.is_some() {
                //     queue.push_back(Some(Rc::clone(node.left.as_ref().unwrap())));
                // }
                // if node.right.is_some() {
                //     queue.push_back(Some(Rc::clone(node.right.as_ref().unwrap())));
                // }
            }
        }
    }
}