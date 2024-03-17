#
# @lc app=leetcode.cn id=1351 lang=python3
#
# [1351] 统计有序矩阵中的负数
#
from sbw import *
# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        ret=0
        idx=C-1

        for r in range(R):
            if idx<0:
                return ret+(R-r)*C
            while idx>=0 and grid[r][idx]<0:
                idx-=1
            ret+=C-idx-1
        return ret
            
# @lc code=end
assert Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])==8
