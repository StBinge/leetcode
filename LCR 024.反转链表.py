#
# @lc app=leetcode.cn id=LCR 024 lang=python3
# @lcpr version=30204
#
# [LCR 024] 反转链表
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
    def reverseList(self, head: ListNode) -> ListNode:
        pre=None
        while head:
            nxt=head.next
            head.next=pre
            pre=head
            head=nxt
        return pre
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

