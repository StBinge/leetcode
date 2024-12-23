#
# @lc app=leetcode.cn id=LCR 136 lang=python3
# @lcpr version=30204
#
# [LCR 136] 删除链表的节点
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
    def deleteNode(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(-1,head)
        pre=dummy
        while True:
            if pre.next.val==val:
                pre.next=pre.next.next
                return dummy.next
            pre=pre.next
# @lc code=end



#
# @lcpr case=start
# [4,5,1,9]\n5\n
# @lcpr case=end

# @lcpr case=start
# [4,5,1,9]\n1\n
# @lcpr case=end

#

