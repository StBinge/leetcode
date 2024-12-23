#
# @lc app=leetcode.cn id=LCR 123 lang=python3
# @lcpr version=30204
#
# [LCR 123] 图书整理 I
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
    def reverseBookList(self, head: Optional[ListNode]) -> List[int]:
        ret=[]
        while head:
            ret.append(head.val)
            head=head.next
        return ret[::-1]

# @lc code=end
assert Solution().reverseBookList(ListNode.build([3,6,4,1]))


#
# @lcpr case=start
# [3,6,4,1]\n
# @lcpr case=end

#

