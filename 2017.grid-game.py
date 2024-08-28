#
# @lc app=leetcode.cn id=2017 lang=python3
# @lcpr version=30204
#
# [2017] 网格游戏
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N=len(grid[0])
        s1=sum(grid[0])
        s2=0
        ret=float('inf')
        for i in range(N):
            s1-=grid[0][i]
            ret=min(ret,max(s1,s2))
            s2+=grid[1][i]
        return ret

# @lc code=end
assert Solution().gridGame([[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]])==63
assert Solution().gridGame([[2,5,4],[1,5,1]])==4


#
# @lcpr case=start
# [[2,5,4],[1,5,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,3,1],[8,5,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,1,15],[1,3,3,1]]\n
# @lcpr case=end

#

