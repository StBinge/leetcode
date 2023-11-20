#
# @lc app=leetcode.cn id=407 lang=python3
#
# [407] 接雨水 II
#
from typing import List
# @lc code=start
import heapq
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        R=len(heightMap)
        C=len(heightMap[0])
        if R<=2 or C<=2:
            return 0
        ret=0
        maxH=max(heightMap[0])
        for r in range(1,R):
            maxH=max(maxH,max(heightMap[r]))
        waters=[[maxH]*C for _ in range(R)]
        queue=[]
        for r in range(R):
            for c in range(C):
                if r==0 or r==R-1 or c==0 or c==C-1:
                    if heightMap[r][c]<waters[r][c]:
                        waters[r][c]=heightMap[r][c]
                        queue.append([r,c])
        dirs=[-1,0,1,0,-1]
        while queue:
            r,c=queue.pop()
            for k in range(4):
                nr,nc=r+dirs[k],c+dirs[k+1]
                if nr<0 or nr>=R or nc<0 or nc>=C:
                    continue
                if waters[nr][nc]>waters[r][c]:
                    waters[nr][nc]=max(waters[r][c],heightMap[nr][nc])
                    queue.append([nr,nc])
        for r in range(R):
            for c in range(C):
                ret+=waters[r][c]-heightMap[r][c]
        return ret
# @lc code=end
heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
assert Solution().trapRainWater(heightMap)==10


heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
assert Solution().trapRainWater(heightMap)==4