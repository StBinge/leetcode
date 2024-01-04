#
# @lc app=leetcode.cn id=1019 lang=python3
#
# [1019] 链表中的下一个更大节点
#
from sbw import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack=[]
        cur=head
        ret=[]
        while cur:
            v=cur.val
            while stack and v>stack[-1][1]:
                idx,_=stack.pop()
                ret[idx]=v
            stack.append([len(ret),v])
            ret.append(0)
            cur=cur.next
        return ret
# @lc code=end
head = [2,7,4,3,5]
ret=[7,0,5,5,0]
assert Solution().nextLargerNodes(ListNode.build(head))==ret

head = [2,1,5]
ret=[5,5,0]
assert Solution().nextLargerNodes(ListNode.build(head))==ret
