#
# @lc app=leetcode.cn id=2127 lang=python3
# @lcpr version=30204
#
# [2127] 参加会议的最多员工数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        N=len(favorite)
        deg=[0]*N
        for i,f in enumerate(favorite):
            deg[f]+=1
        mx=mx_id=0
        for i,f in enumerate(deg):
            
# @lc code=end



#
# @lcpr case=start
# [2,2,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [3,0,1,4,1]\n
# @lcpr case=end

#

