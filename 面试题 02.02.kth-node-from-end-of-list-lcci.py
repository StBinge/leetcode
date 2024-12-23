#
# @lc app=leetcode.cn id=面试题 02.02 lang=python3
# @lcpr version=30204
#
# [面试题 02.02] 返回倒数第 k 个节点
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
    def kthToLast(self, head: Optional[ListNode], k: int) -> int:
        fast=head
        while k:
            fast=fast.next
            k-=1
        slow=head
        while fast:
            fast=fast.next
            slow=slow.next
        return slow.val
# @lc code=end
assert Solution().kthToLast(ListNode.build([1,2,3,4,5]),2)==4


#
# @lcpr case=start
# 2\n
# @lcpr case=end

#

