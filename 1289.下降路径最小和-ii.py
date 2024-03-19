#
# @lc app=leetcode.cn id=1289 lang=python3
#
# [1289] 下降路径最小和  II
#
from sbw import *
# @lc code=start
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m1,m2=0,0
        # i1,i2=-1,-1
        mi=-1
        for row in grid:
            cur1=cur2=float('inf')
            j=-1
            for i,n in enumerate(row):
                if i==mi:
                    cur=n+m2
                else:
                    cur=n+m1
                if cur<cur1:
                    cur1,cur2=cur,cur1
                    j=i
                elif cur<cur2:
                    cur2=cur
            m1,m2=cur1,cur2
            mi=j


        return m1
# @lc code=end
grid=[[1]+[99]*198+[1] for _ in range(200)]
assert Solution().minFallingPathSum(grid)==200
assert Solution().minFallingPathSum([[-73,61,43,-48,-36],[3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]])==-192
assert Solution().minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]])==13
assert Solution().minFallingPathSum([[7]])==7
