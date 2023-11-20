#
# @lc app=leetcode.cn id=725 lang=python3
#
# [725] 分隔链表
#
from sbw import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if not head:
            return [None]*k
        cur=head
        cnt=0
        while cur:
            cnt+=1
            cur=cur.next
        avg=cnt//k
        remaning=cnt%k
        ret=[]
        cur=head
        for i in range(k):
            ret.append(cur)
            if not cur:
                continue
            length=avg
            if remaning:
                length+=1
                remaning-=1
            for _ in range(length-1):
                cur=cur.next
            if not cur:
                continue
            temp=cur.next
            cur.next=None
            cur=temp
        return ret
# @lc code=end
head = [1,2,3]
k = 5
ret= Solution().splitListToParts(ListNode.build(head),k)
pass

head = [1,2,3,4,5,6,7,8,9,10]
k = 3
ret= Solution().splitListToParts(head,k)
pass