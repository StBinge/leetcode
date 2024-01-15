#
# @lc app=leetcode.cn id=1072 lang=python3
#
# [1072] 按列翻转得到最大值等行数
#
from sbw import *
# @lc code=start
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cnt={}
        for row in matrix:
            key=0
            for c in row:
                key=key*10+c^row[0]
            cnt[key]=cnt.get(key,0)+1
        return max(cnt.values())
# @lc code=end
assert Solution().maxEqualRowsAfterFlips(matrix = [[0,0,0],[0,0,1],[1,1,0]])==2
assert Solution().maxEqualRowsAfterFlips(matrix = [[0,1],[1,1]])==1
assert Solution().maxEqualRowsAfterFlips(matrix = [[0,1],[1,0]])==2
