#
# @lc app=leetcode.cn id=2181 lang=python3
# @lcpr version=30204
#
# [2181] 合并零之间的节点
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
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail=head
        cur=head.next
        while cur.next:
            if cur.val==0:
                tail=tail.next
                tail.val=0
            else:
                tail.val+=cur.val
            cur=cur.next
        tail.next=None
        return head

# @lc code=end



#
# @lcpr case=start
# [0,3,1,0,4,5,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,3,0,2,2,0]\n
# @lcpr case=end

#

