#
# @lc app=leetcode.cn id=1171 lang=python3
#
# [1171] 从链表中删去总和值为零的连续节点
#
from sbw import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        presum=0
        memo={0:dummy}
        while head:
            presum+=head.val
            memo[presum]=head
            head=head.next

        head=dummy
        s=0
        while head:
            s+=head.val
            head.next=memo[s].next
            head=head.next
        return dummy.next

# @lc code=end
assert Solution().removeZeroSumSublists(ListNode.build([1,2,3,-3,-2])).to_list()==[1]
assert Solution().removeZeroSumSublists(ListNode.build([1,2,3,-3,4])).to_list()==[1,2,4]
assert Solution().removeZeroSumSublists(ListNode.build([1,2,-3,3,1])).to_list()==[3,1]
