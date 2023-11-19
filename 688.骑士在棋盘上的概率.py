#
# @lc app=leetcode.cn id=688 lang=python3
#
# [688] 骑士在棋盘上的概率
#

# @lc code=start
# from collections import deque
# from functools import lru_cache
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k==0:
            return 1
        dp=[[[0]*n for _ in range(n) ]for _ in range(k+1)]
        # dp[0][row][column]=1
        for s in range(k+1):
            for r in range(n):
                for c in range(n):
                    if s==0:
                        dp[s][r][c]=1
                        continue
                    for di, dj in ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)):
                        nr,nc=r+di,c+dj
                        if 0<=nr<n and 0<=nc<n:
                            dp[s][nr][nc]+=dp[s-1][r][c]/8
        return dp[k][row][column]
# @lc code=end
ret=Solution().knightProbability(3,2,0,0)
assert ret==0.0625
ret=Solution().knightProbability(8,30,6,4)
assert ret==0.00019
assert Solution().knightProbability(1,0,0,0)==1
