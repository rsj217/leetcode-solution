use crate::datastruct::linknode::ListNode;

pub struct Solution {}


impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut node = head;
        let mut prev = None;
        while let Some(mut curnode) = node {
            node = curnode.next.take();
            curnode.next = prev;
            prev = Some(curnode);
        }
        prev
    }
}

#[cfg(test)]
mod tests {
    use super::*;


    #[test]
    fn test_solution() {
        let test_case = vec![
            (vec![1, 2, 3, 4, 5]),
        ];
        for nums in test_case {
            let head = ListNode::create(nums);
            let ans = Solution::reverse_list(head);
            println!("{:?}", ans.unwrap().to_vec())
            // assert_eq!(vec![1, 2, 3, 4,5], nums.reverse());
        }
    }
}
