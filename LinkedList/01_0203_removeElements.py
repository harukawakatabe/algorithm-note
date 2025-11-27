# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        cur = dummy_head
        while cur.next != None:     # Point: 必须考虑如何移动指针，否则while会死循环
            if cur.next.val == val: # Point: 如果找到目标，直接赋值
                cur.next = cur.next.next
            # 如果没有找到目标，需要移动指针！！
            else:
                cur = cur.next
        return dummy_head.next  # Point: 返回dummy_head.next


"""
思路
    main
        1.将下下个节点直接赋值给当前节点的next
    虚拟头
        1.使用虚拟头节点统一删除头节点和删除非头节点的操作
        2.使用新指针cur遍历链表
        3.*返回dummy_head.next
Point
1.必须考虑如何移动指针，否则while会死循环
"""