#
# @lc app=leetcode.cn id=2058 lang=python3
# @lcpr version=30204
#
# [2058] 找出临界点之间的最小和最大距离
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
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        min_dist=float('inf')
        max_dist=0
        cur=head
        first_point=-1
        pre_point=-1
        idx=1
        while cur.next.next:
            pre_val=cur.val
            mid_val=cur.next.val
            nxt_val=cur.next.next.val
            if (pre_val<mid_val and nxt_val<mid_val) or (pre_val>mid_val and nxt_val>mid_val):
                if pre_point!=-1:
                    min_dist=min(min_dist,idx-pre_point)
                    max_dist=idx-first_point
                pre_point=idx
                if first_point==-1:
                    first_point=idx
            idx+=1
            cur=cur.next
        if max_dist>0:
            return [min_dist,max_dist]
        return [-1,-1]

# @lc code=end
assert Solution().nodesBetweenCriticalPoints(ListNode.build([5,3,1,2,5,1,2]))==[1,3]


#
# @lcpr case=start
# [3,1]\n
# @lcpr case=end

# @lcpr case=start
# [5,3,1,2,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,2,2,3,2,2,2,7]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,3,2]\n
# @lcpr case=end

#

