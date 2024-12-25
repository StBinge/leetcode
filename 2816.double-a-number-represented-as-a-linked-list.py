#
# @lc app=leetcode.cn id=2816 lang=python3
# @lcpr version=30204
#
# [2816] 翻倍以链表形式表示的数字
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
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val>4:
            head=ListNode(0,head)
        cur=head
        while cur:
            cur.val=(cur.val*2)%10
            if cur.next and cur.next.val>4:
                cur.val+=1
            cur=cur.next
        return head
# @lc code=end



#
# @lcpr case=start
# [1,8,9]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9]\n
# @lcpr case=end

#

