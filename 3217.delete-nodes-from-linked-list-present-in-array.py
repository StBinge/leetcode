#
# @lc app=leetcode.cn id=3217 lang=python3
# @lcpr version=30204
#
# [3217] 从链表中移除在数组中存在的节点
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
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums=set(nums)
        dummy=ListNode(0,head)
        cur=dummy
        while cur.next:
            if cur.next.val in nums:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return dummy.next
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n[1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n[1,2,1,2,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [5]\n[1,2,3,4]\n
# @lcpr case=end

#

