#
# @lc app=leetcode.cn id=1290 lang=python3
#
# [1290] 二进制链表转整数
#
from sbw import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ret=0
        while head:
            ret=(ret<<1) +head.val
            head=head.next
        return ret
        
# @lc code=end
assert Solution().getDecimalValue(ListNode.build([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]))==18880
