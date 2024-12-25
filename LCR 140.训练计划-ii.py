#
# @lc app=leetcode.cn id=LCR 140 lang=python3
# @lcpr version=30204
#
# [LCR 140] 训练计划 II
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        fast=head
        for i in range(cnt):
            fast=fast.next
        slow=head
        while fast:
            fast=fast.next
            slow=slow.next
        return slow
# @lc code=end



#
# @lcpr case=start
# [2,4,7,8]\n1\n
# @lcpr case=end

#

