#
# @lc app=leetcode.cn id=1030 lang=python3
#
# [1030] 距离顺序排列矩阵单元格
#
from sbw import *
# @lc code=start
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        max_dist=max(rCenter,rows-1-rCenter)+max(cCenter,cols-1-cCenter)
        buckets=[[] for _ in range(max_dist+1)]
        for r in range(rows):
            for c in range(cols):
                buckets[abs(r-rCenter)+abs(c-cCenter)].append([r,c])
        ret=[]
        for d in range(max_dist+1):
            ret.extend(buckets[d])
        return ret
# @lc code=end
print(Solution().allCellsDistOrder(2,2,0,1))
rows = 1
cols = 2
rCenter = 0
cCenter = 0
#输出：[[0,0],[0,1]]
print(Solution().allCellsDistOrder(rows,cols,rCenter,cCenter))
