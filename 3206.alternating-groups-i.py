#
# @lc app=leetcode.cn id=3206 lang=python3
# @lcpr version=30204
#
# [3206] 交替组 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        N=len(colors)
        ret=0
        for i in range(N):
            ret+=colors[(i-1)%N]==colors[(i+1)%N] and colors[(i-1)%N]!=colors[i]
        return ret
# @lc code=end



#
# @lcpr case=start
# [1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,0,1]\n
# @lcpr case=end

#

