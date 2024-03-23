#
# @lc app=leetcode.cn id=1267 lang=python3
#
# [1267] 统计参与通信的服务器
#
from sbw import *
# @lc code=start
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ret=0
        R,C=len(grid),len(grid[0])
        rows=[0]*R
        cols=[0]*C
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1:
                    rows[r]+=1
                    cols[c]+=1
        for r in range(R):
            if rows[r]==1:
                for c in range(C):
                    if grid[r][c]==1:
                        if cols[c]>1:
                            ret+=1
                        break
            elif rows[r]>1:
                ret+=rows[r]
        return ret
# @lc code=end
assert Solution().countServers(grid = [[1,0],[1,1]])==3
assert Solution().countServers(grid = [[1,0],[0,1]])==0
