#
# @lc app=leetcode.cn id=1334 lang=python3
#
# [1334] 阈值距离内邻居最少的城市
#
from sbw import *
# @lc code=start
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # w=[[distanceThreshold+1]*n for _ in range(n)]
        f=[[[distanceThreshold+1]*n for _ in range(n)] for _ in range(n+1)]
        for s,e,d in edges:
            f[0][s][e]=f[0][e][s]=d
        
        for k in range(1,n+1):
            for i in range(n):
                for j in range(n):
                    f[k][i][j]=min(f[k-1][i][j],f[k-1][i][k-1]+f[k-1][k-1][j])
        min_cnt=n+1
        ret=-1
        cnt=[0]*n
        for i in range(n):
            for j in range(i+1,n):
                if f[n][i][j]<=distanceThreshold:
                    cnt[i]+=1
                    cnt[j]+=1
            if cnt[i]<=min_cnt:
                ret=i
                min_cnt=cnt[i]
        return ret
# @lc code=end
assert Solution().findTheCity(n = 8, edges = [[3,5,9558],[1,2,1079],[1,3,8040],[0,1,9258],[4,7,7558],[5,6,8196],[3,4,7284],[1,5,6327],[0,4,5966],[3,6,8575],[2,5,8604],[1,7,7782],[4,6,2857],[3,7,2336],[0,6,6],[5,7,2870],[4,5,5055],[0,7,2904],[1,6,2458],[0,5,3399],[6,7,2202],[0,2,3996],[0,3,7495],[1,4,2262],[2,6,1390]], distanceThreshold = 7937)==7
assert Solution().findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2)==0
assert Solution().findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4)==3
