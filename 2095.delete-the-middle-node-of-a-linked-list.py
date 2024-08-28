#
# @lc app=leetcode.cn id=2095 lang=python3
# @lcpr version=30204
#
# [2095] 删除链表的中间节点
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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        slow=dummy
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        slow.next=slow.next.next
        return dummy.next
# @lc code=end



#
# @lcpr case=start
# [1,3,4,7,1,2,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n
# @lcpr case=end

#

