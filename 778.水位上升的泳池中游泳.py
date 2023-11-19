#
# @lc app=leetcode.cn id=778 lang=python3
#
# [778] 水位上升的泳池中游泳
#
from typing import List
# @lc code=start
# from collections import deque
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N=len(grid)
        # visited={(0,0):grid[0,0]}
        queue=[]
        queue.append([grid[0][0],0,0])
        visited=set()
        visited.add((0,0))
        # time=0
        while queue:
            h,r,c=heapq.heappop(queue)
            if r==N-1 and c==N-1:
                return h
            dirs=[-1,0,1,0,-1]
            for i in range(4):
                nr,nc=r+dirs[i],c+dirs[i+1]
                # cid=nr*N+nc
                if nr<0 or nr==N or nc<0 or nc==N or (nr,nc) in visited:
                    continue
                nh=max(h,grid[nr][nc])
                heapq.heappush(queue,[nh,nr,nc])
                visited.add((nr,nc))
                # if visited.get((nr,nc),N**2)>nh:
                #     heapq.heappush(queue,[nh,nr,nc])
                #     visited[(nr,nc)]=nh


# @lc code=end
grid=[[3,2],[0,1]]
assert Solution().swimInWater(grid)==3

grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
assert Solution().swimInWater(grid)==16
grid = [[0,2],[1,3]]
assert Solution().swimInWater(grid)==3
