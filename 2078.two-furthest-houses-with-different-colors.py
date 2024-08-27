#
# @lc app=leetcode.cn id=2078 lang=python3
# @lcpr version=30204
#
# [2078] 两栋颜色不同且距离最远的房子
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        N=len(colors)
        if colors[0]!=colors[-1]:
            return N-1
        ret=0
        for i in range(N-1,0,-1):
            if colors[i]!=colors[0]:
                ret=i
                break
        for i in range(N-1):
            if colors[i]!=colors[-1]:
                ret=max(ret,N-1-i)
                break
        return ret
        
# @lc code=end



#
# @lcpr case=start
# [1,1,1,6,1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,8,3,8,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

#

