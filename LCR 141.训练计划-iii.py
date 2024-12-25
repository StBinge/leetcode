#
# @lc app=leetcode.cn id=LCR 141 lang=python3
# @lcpr version=30204
#
# [LCR 141] 训练计划 III
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
    def trainningPlan(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre=None
        cur=head
        while cur:
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt
        return pre
# @lc code=end
assert Solution().trainningPlan(ListNode.build([])).to_list()==[]
assert Solution().trainningPlan(ListNode.build([1,2,3,4,5])).to_list()==[5,4,3,2,1]


#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

