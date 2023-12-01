#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#
from sbw import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
# @lc code=end
head=ListNode.build([1,2,3,4,5,6])
Solution().middleNode(head).print()
head=ListNode.build([1,2,3,4,5])
Solution().middleNode(head).print()
