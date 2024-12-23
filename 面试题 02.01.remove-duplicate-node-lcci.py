#
# @lc app=leetcode.cn id=面试题 02.01 lang=python3
# @lcpr version=30204
#
# [面试题 02.01] 移除重复节点
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
    def removeDuplicateNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen=set()
        dummy=ListNode(-1,head)
        cur=dummy
        while cur.next:
            if cur.next.val not in seen:
                seen.add(cur.next.val)
                cur=cur.next
            else:
                cur.next=cur.next.next
        return dummy.next
# @lc code=end



#
# @lcpr case=start
# [1, 2, 3, 3, 2, 1]\n
# @lcpr case=end

# @lcpr case=start
# [1, 1, 1, 1, 2]\n
# @lcpr case=end

#

