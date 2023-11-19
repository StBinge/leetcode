#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=0
        while l1:
            n1=n1*10+l1.val
            l1=l1.next
        
        n2=0
        while l2:
            n2=n2*10+l2.val
            l2=l2.next
        s=n1+n2
        if s==0:
            return ListNode(0)
        tens=1
        while tens<=s:
            tens*=10
        tens//=10
        dummy=ListNode()
        cur=dummy
        while tens>0:
            cur.next=ListNode(s//tens)
            s%=tens
            tens//=10
            cur=cur.next
        return dummy.next
# @lc code=end

