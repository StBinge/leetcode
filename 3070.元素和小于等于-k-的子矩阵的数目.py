#
# @lc app=leetcode.cn id=3070 lang=python3
#
# [3070] 元素和小于等于 k 的子矩阵的数目
#
from sbw import *
# @lc code=start
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        R,C=len(grid),len(grid[0])
        # presums=[[0]*C]
        ret=0
        col_sum=[0]*C
        for r in range(R):
            if col_sum[0]>k:
                break
            v=0
            for c in range(C):
                col_sum[c]+=grid[r][c]
                v+=col_sum[c]
                if v<=k:
                    ret+=1
                else:
                    break
        return ret
# @lc code=end

assert Solution().countSubmatrices([[6],[5]],9)==1
assert Solution().countSubmatrices(grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20)==6
assert Solution().countSubmatrices(grid = [[7,6,3],[6,6,1]], k = 18)==4