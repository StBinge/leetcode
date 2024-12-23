#
# @lc app=leetcode.cn id=面试题 02.06 lang=python3
# @lcpr version=30204
#
# [面试题 02.06] 回文链表
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        L=0
        _head=head
        while _head:
            L+=1
            _head=_head.next
        
        mid=(L+1)//2
        _head=head
        for i in range(mid):
            _head=_head.next
        
        pre=None
        while _head:
            nxt=_head.next
            _head.next=pre
            pre=_head
            _head=nxt
        while pre:
            if pre.val!=head.val:
                return False
            pre=pre.next
            head=head.next
        return True
# @lc code=end
assert Solution().isPalindrome(ListNode.build([1,2,2,1]))
assert Solution().isPalindrome(ListNode.build([1,2]))==False

#
# @lcpr case=start
# 1->2\n
# @lcpr case=end

# @lcpr case=start
# 1->2->2->1\n
# @lcpr case=end

#

