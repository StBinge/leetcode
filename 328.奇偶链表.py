#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#
from typing import *
from sbw import *

# @lc code=start
# Definition for singly-linked list.
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        even_head=head.next
        odd,even=head,even_head
        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=even_head
        return head
        
# @lc code=end

head=ListNode.build([1,2,3,4,5])
Solution().oddEvenList(head).display()

head=ListNode.build([2,1,3,5,6,4,7])
Solution().oddEvenList(head).display()