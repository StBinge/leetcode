#
# @lc app=leetcode.cn id=382 lang=python3
#
# [382] 链表随机节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head=head
        # cnt=0
        # while head:
        #     cnt+=1
        #     head=head.next
        # self.length=cnt

    def getRandom(self) -> int:
        # idx=random.randint(0,self.length-1)
        # head=self.head
        # while idx>0:
        #     head=head.next
        #     idx-=1
        # return head.val
        head=self.head
        ans,i=head.val,0
        while head:
            if random.randint(0,i)==0:
                ans=head.val
            i+=1
            head=head.next
        return ans



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

