#
# @lc app=leetcode.cn id=1824 lang=python3
#
# [1824] 最少侧跳次数
#
from sbw import *
# @lc code=start
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        N=len(obstacles)
        # f=[[float('inf')]*3 for _ in range(N)]
        # f[0][1]=0
        Max=float('inf')
        f=[1,0,1]
        for flag in obstacles:
            if flag!=0:
                f[flag-1]=Max
            mi=min(f)
            for i in range(3):
                if i!=flag-1:
                    f[i]=min(f[i],mi+1)

        return min(f)
# @lc code=end
assert Solution().minSideJumps(obstacles = [0,1,2,3,0])==2
assert Solution().minSideJumps([0,2,1,0,3,0])==2
assert Solution().minSideJumps([0,1,1,3,3,0])==0
