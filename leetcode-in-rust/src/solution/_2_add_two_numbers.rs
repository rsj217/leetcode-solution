use crate::datastruct::linknode::ListNode;

pub struct Solution;

impl Solution {
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let (mut l1, mut l2) = (l1, l2);

        let mut carry = 0;
        let mut head = ListNode::new(0);
        let mut node = &mut head;

        while l1.is_some() || l2.is_some() || carry != 0 {
            let mut sum = carry;

            if let Some(list_node) = l1 {
                sum += list_node.val;
                l1 = list_node.next
            }

            if let Some(list_node) = l2 {
                sum += list_node.val;
                l2 = list_node.next;
            }
            carry = sum / 10;
            node.next = Some(Box::new(ListNode::new(sum % 10)));
            node = node.next.as_mut().unwrap();
        }
        head.next
    }
}

#[cfg(test)]
mod tests {
    use crate::datastruct::linknode::ListNode;
    use super::*;

    #[test]
    fn test_solution() {
        let test_case = vec![
            (vec![2, 4, 3], vec![5, 6, 4], vec![7, 0, 8]),
            (vec![9, 9, 9, 9, 9, 9, 9], vec![9, 9, 9, 9], vec![8, 9, 9, 9, 0, 0, 0, 1]),
        ];

        for (num1, num2, num3) in test_case {
            let l1 = ListNode::create(num1);
            let l2 = ListNode::create(num2);
            let answer = ListNode::create(num3);
            let ans = Solution::add_two_numbers(l1, l2);
            assert_eq!(ans, answer)
        }
    }
}
