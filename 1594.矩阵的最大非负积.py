#
# @lc app=leetcode.cn id=1594 lang=python3
#
# [1594] 矩阵的最大非负积
#
from sbw import *


# @lc code=start
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        Mod=10**9+7

        # min,max
        f0=[None for _ in range(C)]
        mi,ma=1,1
        for c in range(C):
            v=grid[0][c]
            if v>=0:
                mi,ma=mi*v,ma*v
            else:
                mi,ma=ma*v,mi*v
            f0[c]=[mi,ma]
        f1=[[1,1] for _ in range(C)]
        for r in range(1,R):
            mi,ma=f0[0][0]*grid[r][0],f0[0][1]*grid[r][0]
            if mi>ma:
                mi,ma=ma,mi
            f1[0]=[mi,ma]
            for c in range(1,C):               

                mi=min(f0[c][0],f1[c-1][0],mi)
                ma=max(f0[c][1],f1[c-1][1],ma)
                v=grid[r][c]
                if v>=0:
                    mi,ma=mi*v,ma*v
                if v<0:
                    mi,ma=ma*v,mi*v
                # ma=module(ma)
                # mi=module(mi)
                f1[c]=[mi,ma]
            f0,f1=f1,f0
        return  f0[-1][1]%Mod if f0[-1][1]>=0 else -1


# @lc code=end
assert Solution().maxProductPath([[1,-1,0,-3,4,3,-3,3,-1,3,0,0,-4,2],[2,-2,-3,-4,0,-2,-3,3,1,4,1,-3,-1,-4],[-4,4,-4,-4,2,-4,3,0,-2,-4,3,4,-1,0],[-3,3,-4,-4,3,4,4,1,-1,-1,0,3,4,1],[1,3,-4,2,2,-3,1,-3,-4,-4,-1,-4,-4,4],[1,1,-1,1,-1,-1,3,-4,-1,2,-2,3,-4,0],[1,0,3,3,1,4,1,1,-4,-1,-3,4,-4,4],[4,3,2,3,0,-1,2,-4,1,0,0,1,3,4],[-4,4,-4,-4,2,-2,2,-1,0,-2,2,4,-2,-1],[-2,3,4,-4,3,3,-2,-1,0,-3,4,-2,-1,-4],[4,3,3,3,-3,1,2,-4,-1,4,-3,-3,2,0],[3,3,0,1,-4,-4,-3,3,-2,-4,2,4,-3,3],[-3,0,1,3,0,0,0,-4,-1,4,-1,-3,1,1],[-1,4,0,-3,1,-3,-1,2,1,-3,-1,-4,4,1]]) == 31136867
assert Solution().maxProductPath([[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]]) == -1
assert Solution().maxProductPath([[1, 3], [0, -4]]) == 0
assert Solution().maxProductPath([[1, -2, 1], [1, -2, 1], [3, -4, 1]]) == 8
