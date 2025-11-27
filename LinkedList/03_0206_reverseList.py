# 25/11/27
"""
https://leetcode.cn/problems/reverse-linked-list/description/

● 今日学习的文章链接和视频链接
● 自己看到题目的第一想法
● 看完代码随想录之后的想法 
● 自己实现过程中遇到哪些困难 
● 今日收获，记录一下自己的学习时长

# 25/11/27
# 想法：使用一个循环来反转
# 

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = head
        pre = None
        # 终止条件
        while cur:
            # 存
            tmp = cur.next
            # 反转
            cur.next = pre
            # 移动
            pre = cur
            cur = tmp
        return pre






# # 递归写法
# class Solution(object):
#     def reverse(self,cur,pre):
#         # 先判断结束
#         if cur == None:
#             return pre
#         tmp = cur.next
#         cur.next = pre
#         return self.reverse(tmp,cur) # 需要将处理完的值return出去


#     def reverseList(self, head):
#         """
#         :type head: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         return self.reverse(head,None)