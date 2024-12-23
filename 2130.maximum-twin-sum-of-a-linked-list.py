#
# @lc app=leetcode.cn id=2130 lang=python3
# @lcpr version=30204
#
# [2130] 链表最大孪生和
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
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head.next
        while fast.next:
            fast=fast.next.next
            slow=slow.next
        
        cur=slow.next
        slow.next=None
        pre=None
        while cur:
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt
        
        ret=0
        while head:
            ret=max(ret,head.val+pre.val)
            head=head.next
            pre=pre.next
        return ret

# @lc code=end



#
# @lcpr case=start
# [5,4,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,100000]\n
# @lcpr case=end

#

