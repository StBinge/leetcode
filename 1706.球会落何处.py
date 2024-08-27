#
# @lc app=leetcode.cn id=1706 lang=python3
#
# [1706] 球会落何处
#
from sbw import *
# @lc code=start
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        R,C=len(grid),len(grid[0])
        ret=[-1]*C
        for c in range(C):
            ans=c
            for row in grid:
                dir=row[ans]
                ans+=dir
                if ans<0 or ans==C or row[ans]!=dir:
                    break
            else:
                ret[c]=ans
        return ret

# @lc code=end
assert Solution().findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]])==[1,-1,-1,-1,-1]
assert Solution().findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]])==[0,1,2,3,4,-1]
assert Solution().findBall([[-1]])==[-1]
