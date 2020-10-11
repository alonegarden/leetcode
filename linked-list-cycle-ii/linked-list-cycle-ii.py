#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
# https://leetcode-cn.com/problems/linked-list-cycle-ii/
# 142. 环形链表 II

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

说明：不允许修改给定的链表。



思路小结：

1. 用双指针， a为环前的节点个数 b为环节点个数。 
2. fast指钟走两步， slow指针走一步， 所以fast=2*slow.有环就会相遇。 
3. fast比slow多走了n环。 所 fast=s+bn。 所以 fast = 2nb slow = bn.
4. 相遇说明有环， 第一步已经完成， 第二步是找出入口点。 
5. 把fast恢复到head, fast走a步，show走 nb+a。因为 nb是环，所以，fast和slow又相遇了。 
6. 这时的位置就是入口点



"""   
"""
要定义链表 才可以执行
"""

def detectCycle(head):
    fast, slow = head, head
    while True:
        if not (fast and fast.next): return
        fast, slow = fast.next.next, slow.next
        if fast == slow: break
    fast = head
    while fast != slow:
        fast, slow = fast.next, slow.next
    return fast


if __name__ == '__main__':
    head = [3,2,0,-4]
    print(detectCycle(head))




