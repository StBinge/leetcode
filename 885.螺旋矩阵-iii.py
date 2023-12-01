#
# @lc app=leetcode.cn id=885 lang=python3
#
# [885] 螺旋矩阵 III
#
from typing import List
# @lc code=start
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # vis=set((rStart,cStart))
        ret=[[rStart,cStart]]
        dirs=[
            [0,1],
            [1,0],
            [0,-1],
            [-1,0]
        ]
        d=0
        r,c=rStart,cStart
        total=rows*cols
        if total==1:
            return ret
        steps=1
        while True:
            for i in range(2):
                for _ in range(steps):
                    r,c=r+dirs[d][0],c+dirs[d][1]
                    if 0<=r<rows and 0<=c<cols:
                        ret.append([r,c])
                        if len(ret)==total:
                            return ret
                d=(d+1)%4
            steps+=1
        # return ret

# @lc code=end
rows = 5
cols = 6
rStart = 1
cStart = 4
ret=[[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
assert Solution().spiralMatrixIII(rows,cols,rStart,cStart)==ret

rows = 1
cols = 4
rStart = 0
cStart = 0
ret=[[0,0],[0,1],[0,2],[0,3]]
assert Solution().spiralMatrixIII(rows,cols,rStart,cStart)==ret

rows = 1
cols = 1
rStart = 0
cStart = 0
ret=[[0,0]]
assert Solution().spiralMatrixIII(rows,cols,rStart,cStart)==ret