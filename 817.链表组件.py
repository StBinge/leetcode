#
# @lc app=leetcode.cn id=817 lang=python3
#
# [817] 链表组件
#
from sbw import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums_set=set(nums)
        ret=0
        inset=False
        while head:
            if head.val in nums_set:
                if not inset:
                    inset=True
                    ret+=1
            else:
                inset=False
            head=head.next
        return ret

# @lc code=end
head = [0,1,2,3]
nums = [0,1,3]
assert Solution().numComponents(ListNode.build(head),nums)==2
head = [0,1,2,3,4]
nums = [0,3,1,4]
assert Solution().numComponents(ListNode.build(head),nums)==2
