#
# @lc app=leetcode.cn id=2536 lang=python3
# @lcpr version=30204
#
# [2536] 子矩阵元素加 1
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        dif=[[0]*(n+2) for _ in range(n+2)]
        for r1,c1,r2,c2 in queries:
            dif[r1+1][c1+1]+=1
            dif[r1+1][c2+2]-=1
            dif[r2+2][c1+1]-=1
            dif[r2+2][c2+2]+=1
        
        for r in range(1,n+1):
            for c in range(1,n+1):
                dif[r][c]+=dif[r][c-1]+dif[r-1][c]-dif[r-1][c-1]
        
        dif=dif[1:-1]
        for r in range(n):
            dif[r]=dif[r][1:-1]
        return dif
# @lc code=end
assert Solution().rangeAddQueries(n = 3, queries = [[1,1,2,2],[0,0,1,1]])==[[1,1,0],[1,2,1],[0,1,1]]


#
# @lcpr case=start
# 3\n[[1,1,2,2],[0,0,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[0,0,1,1]]\n
# @lcpr case=end

#

