#
# @lc app=leetcode.cn id=1368 lang=python3
#
# [1368] 使网格图至少有一条有效路径的最小代价
#
from sbw import *
# @lc code=start
import heapq
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        vis=[[False]*C for _ in range(R)]
        # vis[0][0]=True
        dirs=[
            [0,0],
            [0,1],
            [0,-1],
            [1,0],
            [-1,0]
        ]
        dis=[[R*C]*C for _ in range(R)]
        dis[0][0]=0
        q=deque([[0,0]])
        while q:
            x,y=q.popleft()

            if vis[x][y]:
                continue
            vis[x][y]=True
            cur_dir=grid[x][y]
            for i in range(1,5):
                dx,dy=dirs[i]
                nx,ny=x+dx,y+dy
                nxt_dis=dis[x][y]+int(i!=cur_dir)
                if 0<=nx<R and 0<=ny<C and dis[nx][ny]>nxt_dis:
                    dis[nx][ny]=nxt_dis
                    if i==cur_dir:
                        q.appendleft([nx,ny])
                    else:
                        q.append([nx,ny])
        return dis[-1][-1]
# @lc code=end
ret= Solution().minCost([[3,4,3],[2,2,2],[2,1,1],[4,3,2],[2,1,4],[2,4,1],[3,3,3],[1,4,2],[2,2,1],[2,1,1],[3,3,1],[4,1,4],[2,1,4],[3,2,2],[3,3,1],[4,4,1],[1,2,2],[1,1,1],[1,3,4],[1,2,1],[2,2,4],[2,1,3],[1,2,1],[4,3,2],[3,3,4],[2,2,1],[3,4,3],[4,2,3],[4,4,4]])
assert ret==18
assert Solution().minCost([[2,2,2],[2,2,2]])==3
assert Solution().minCost([[1,2],[4,3]])==1
assert Solution().minCost([[1,1,3],[3,2,2],[1,1,4]])==0
assert Solution().minCost(grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]])==3
