#
# @lc app=leetcode.cn id=1669 lang=python3
#
# [1669] 合并两个链表
#
from sbw import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        pre1=list1
        for i in range(a-1):
            pre1=pre1.next

        post1=pre1
        for i in range(b-a+2):
            post1=post1.next
        
        pre1.next=list2
        while list2.next:
            list2=list2.next
        list2.next=post1
        return list1
        
# @lc code=end
assert Solution().mergeInBetween(ListNode.build([10,1,13,6,9,5]),3,4,ListNode.build([1000000,1000001,1000002])).to_list()==[10,1,13,1000000,1000001,1000002,5]
