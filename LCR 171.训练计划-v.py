#
# @lc app=leetcode.cn id=LCR 171 lang=python3
# @lcpr version=30204
#
# [LCR 171] 训练计划 V
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
        l1=0
        _a=headA
        while headA:
            l1+=1
            headA=headA.next
        l2=0
        _b=headB
        while headB:
            l2+=1
            headB=headB.next
        
        if l1>l2:
            l1,l2=l2,l1
            _a,_b=_b,_a
        while l2>l1:
            _b=_b.next
            l2-=1
        
        while _a and _b:
            if _a==_b:
                return _a
            _a=_a.next
            _b=_b.next
        return None
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

