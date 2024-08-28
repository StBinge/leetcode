#
# @lc app=leetcode.cn id=1721 lang=python3
#
# [1721] 交换链表中的节点
#
from sbw import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur=head
        for _ in range(k-1):
            cur=cur.next
        first=cur
        tail=cur
        cur=head
        while tail.next:
            tail=tail.next
            cur=cur.next
        first.val,cur.val=cur.val,first.val
        return head
# @lc code=end
assert Solution().swapNodes(ListNode.build([1,2,3,4,5]),2).to_list()==[1,4,3,2,5]
