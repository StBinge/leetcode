#
# @lc app=leetcode.cn id=面试题 02.07 lang=python3
# @lcpr version=30204
#
# [面试题 02.07] 链表相交
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
        la=0
        _heada=headA
        while _heada:
            la+=1
            _heada=_heada.next

        _headb=headB
        lb=0
        while _headb:
            lb+=1
            _headb=_headb.next
        
        if la>lb:
            la,lb=lb,la
            headA,headB=headB,headA
        
        for i in range(lb-la):
            headB=headB.next
        
        while headB and headA:
            if headB==headA:
                return headB
            headB=headB.next
            headA=headA.next
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

