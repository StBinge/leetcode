#
# @lc app=leetcode.cn id=2487 lang=python3
# @lcpr version=30204
#
# [2487] 从链表中移除节点
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
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        nxt = self.removeNodes(head.next)
        if nxt.val > head.val:
            return nxt
        else:
            head.next = nxt
            return head


# @lc code=end
assert Solution().removeNodes(ListNode.build([5, 2, 13, 3, 8])).to_list() == [13, 8]


#
# @lcpr case=start
# [5,2,13,3,8]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1]\n
# @lcpr case=end

#
