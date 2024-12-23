#
# @lc app=leetcode.cn id=LCR 027 lang=python3
# @lcpr version=30204
#
# [LCR 027] 回文链表
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
    def isPalindrome(self, head: ListNode) -> bool:
        N=0
        h=head
        while h:
            N+=1
            h=h.next
        
        h=head
        for i in range(N//2):
            h=h.next
        pre=h
        h=h.next
        while h:
            nxt=h.next
            h.next=pre
            pre=h
            h=nxt
        
        for i in range(N//2):
            if head.val!=pre.val:
                return False
            head=head.next
            pre=pre.next
        return True
# @lc code=end
assert Solution().isPalindrome(ListNode.build([1,2]))==False
assert Solution().isPalindrome(ListNode.build([1,2,3,3,2,1]))


#
# @lcpr case=start
# [1,2,3,3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

