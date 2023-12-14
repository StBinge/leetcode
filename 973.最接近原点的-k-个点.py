#
# @lc app=leetcode.cn id=973 lang=python3
#
# [973] 最接近原点的 K 个点
#
from sbw import *
# @lc code=start
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ret=[]
        for x,y in points:
            dis=x*x+y*y
            if len(ret)<k:
                heapq.heappush(ret,[-dis,x,y])
            else:
                heapq.heappushpop(ret,[-dis,x,y])
        return [[x,y] for _,x,y in ret]
# @lc code=end
points = [[3,3],[5,-1],[-2,4]]
k = 2
ret=[[3,3],[-2,4]]
res=Solution().kClosest(points,k)
assert sorted(res)==sorted(ret)

points = [[1,3],[-2,2]]
k = 1
ret=[[-2,2]]
res=Solution().kClosest(points,k)
assert sorted(res)==sorted(ret)