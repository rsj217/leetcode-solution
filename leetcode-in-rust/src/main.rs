// // use leetcode_in_rust::datastruct::treenode::{TreeNode, print_tree};
// // use std::collections::VecDeque;
// // use std::rc::Rc;
//
// fn main() {
//
//     // let nums = vec![Some(1), Some(2), Some(3), Some(4), None, Some(5), Some(6), None, Some(7), None, None, Some(8)];
//     // let root = TreeNode::create(nums);
//     // let height = TreeNode::get_height(&root);
//     //
//     //
//     // println!("{}", print_tree(root, height as u32, " "));
//
//     // let mut queue = VecDeque::new();
//     // queue.push_back(root);
//     // while !queue.is_empty() {
//     //     let size = queue.len();
//     //     for _i in 0..size {
//     //         if let Some(node) = queue.pop_front().flatten() {
//     //             let node = node.borrow();
//     //             println!("{}", node.val);
//     //             if let Some(ref left) = node.left {
//     //                 queue.push_back(Some(Rc::clone(left)))
//     //             }
//     //             if let Some(ref right) = node.right {
//     //                 queue.push_back(Some(Rc::clone(right)))
//     //             }
//     //         }
//     //     }
//     // }
//     // println!("{}", print_tree(root, height as u32, " "));
//
//
//
//     //
//     // let a = say();
//     //
//     // match a {
//     //
//     //     Some(x) => println!("{}", x),
//     //     None => println!("None"),
//     // }
//
//
//     // println!("{:?}", a);
//
//     // let mut value = String::from("hello");
//     //
//     // let ref2 = &mut value;
//     // let ref1 = &value;
//     // println!("{}", ref1);
//
//     let mut i = 0;
//     let p1 = &mut i;
//     i = 1;
//
//
//
// }
//
//
//

fn main(){
    let mut i = 0;
    let p1 = &i;
    i = 1;
}