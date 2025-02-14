#
# @lc app=leetcode.cn id=2807 lang=python3
# @lcpr version=30204
#
# [2807] 在链表中插入最大公约数
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        while cur.next:
            mid_val=math.gcd(cur.val,cur.next.val)
            node=ListNode(mid_val)
            node.next=cur.next
            cur.next=node
            cur=node.next
        return head
# @lc code=end



#
# @lcpr case=start
# [18,6,10,3]\n
# @lcpr case=end

# @lcpr case=start
# [7]\n
# @lcpr case=end

#

