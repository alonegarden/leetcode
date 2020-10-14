#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/
# 24. 两两交换链表中的节点

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


1 -> 2 -> 3 -> 4
2 -> 1 -> 4 -> 3


思路小结：

1. 两两交换
2. 多多交换

"""

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        p0 = ListNode(0)
        p0.next = head
        pp = p0
        while pp.next and pp.next.next:
            a = pp.next
            b = pp.next.next
            pp.next = b
            a.next = b.next
            b.next = a
            pp = pp.next.next
        return p0.next


if __name__ == '__main__':

   pass

"""
// c++
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
         if (head == nullptr || head->next == nullptr) {
            return head;
        }
        ListNode* newHead = head->next;
        head->next = swapPairs(newHead->next);
        newHead->next = head;
        return newHead;
    }
};
"""



