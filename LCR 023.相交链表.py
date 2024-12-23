#
# @lc app=leetcode.cn id=LCR 023 lang=python3
# @lcpr version=30204
#
# [LCR 023] 相交链表
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        h1,h2=headA,headB
        while h1!=h2:
            h1=h1.next if h1 else headB
            h2=h2.next if h2 else headA
        return h1
# @lc code=end



#
# @lcpr case=start
# 8\n[4,1,8,4,5]\n[5,0,1,8,4,5]\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# 2\n[0,9,1,2,4]\n[3,2,4]\n3\n1\n
# @lcpr case=end

# @lcpr case=start
# 0\n[2,6,4]\n[1,5]\n3\n2\n
# @lcpr case=end

#

