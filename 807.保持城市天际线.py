#
# @lc app=leetcode.cn id=807 lang=python3
#
# [807] 保持城市天际线
#
from typing import List
# @lc code=start
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n=len(grid)
        r_max=[0]*n
        c_max=[0]*n
        for r in range(n):
            r_max[r]=max(grid[r])
            for c in range(n):
                c_max[c]=max(c_max[c],grid[r][c])
        
        ret=0
        for r in range(n):
            for c in range(n):
                h=grid[r][c]
                ret+=min(r_max[r],c_max[c])-h
        return ret
# @lc code=end
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
assert Solution().maxIncreaseKeepingSkyline(grid)==35
