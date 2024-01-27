#
# @lc app=leetcode.cn id=1252 lang=python3
#
# [1252] 奇数值单元格的数目
#
from sbw import *
# @lc code=start
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows=[0]*m
        cols=[0]*n
        for r,c in indices:
            rows[r]+=1
            cols[c]+=1
        cols_odds=sum(c%2 for c in cols)
        rows_odds=sum(r%2 for r in rows)
        return rows_odds*(n-cols_odds)+(m-rows_odds)*cols_odds
# @lc code=end
assert Solution().oddCells(m = 2, n = 2, indices = [[1,1],[0,0]])==0
assert Solution().oddCells(m = 2, n = 3, indices = [[0,1],[1,1]])==6
