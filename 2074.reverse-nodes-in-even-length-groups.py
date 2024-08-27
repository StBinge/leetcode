#
# @lc app=leetcode.cn id=2074 lang=python3
# @lcpr version=30204
#
# [2074] 反转偶数长度组的节点
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
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:

        gid=0
        cur=head
        pre=None
        while cur:   
            cnt=0
            gid+=1
            point=cur
            pre_pioint=None
            while cnt<gid and point:
                pre_pioint,point=point,point.next
                cnt+=1
            
            if cnt&1:
                pre=pre_pioint
                cur=point
            else:
                for _ in range(cnt-1):
                    p_nxt=pre.next
                    c_nxt_nxt=cur.next.next
                    pre.next=cur.next
                    pre.next.next=p_nxt
                    cur.next=c_nxt_nxt
                pre=cur
                cur=cur.next
        return head
            
            

# @lc code=end
ret= Solution().reverseEvenLengthGroups(ListNode.build(list(range(1,11)))).to_list()
assert ret==[1,3,2,4,5,6,10,9,8,7],ret
assert Solution().reverseEvenLengthGroups(ListNode.build([5,2,6,3,9,1,7,3,8,4])).to_list()==[5,6,2,3,9,1,4,8,3,7]
assert Solution().reverseEvenLengthGroups(ListNode.build([1,2,3,4,5])).to_list()==[1,3,2,5,4]
assert Solution().reverseEvenLengthGroups(ListNode.build( [2,1])).to_list()==[2,1]
assert Solution().reverseEvenLengthGroups(ListNode.build([1,1,0,6])).to_list()==[1,0,1,6]
assert Solution().reverseEvenLengthGroups(ListNode.build([1,2,3,4])).to_list()==[1,3,2,4]


#
# @lcpr case=start
# [5,2,6,3,9,1,7,3,8,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,0,6]\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n
# @lcpr case=end

#

