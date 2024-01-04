#
# @lc app=leetcode.cn id=1074 lang=python3
#
# [1074] 元素和为目标值的子矩阵数量
#
from sbw import *
# @lc code=start
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        R,C=len(matrix),len(matrix[0])
        def count(values:list):
            mp={0:1}
            pre=cnt=0
            for v in values:
                pre+=v
                cnt+=mp.get(pre-target,0)
                mp[pre]=mp.get(pre,0)+1
            return cnt

        ret=0
        for top in range(R):
            cols=[0]*C
            for bottom in range(top,R):
                for c in range(C):
                    cols[c]+=matrix[bottom][c]
                ret+=count(cols)
        return ret
# @lc code=end
assert Solution().numSubmatrixSumTarget([[0,0,0,1,1],[1,1,1,0,1],[1,1,1,1,0],[0,0,0,1,0],[0,0,0,1,1]],
0)==28
assert Solution().numSubmatrixSumTarget(matrix = [[904]], target = 0)==0
assert Solution().numSubmatrixSumTarget(matrix = [[1,-1],[-1,1]], target = 0)==5
assert Solution().numSubmatrixSumTarget(matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0)==4
