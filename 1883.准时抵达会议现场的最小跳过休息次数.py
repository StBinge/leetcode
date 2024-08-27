#
# @lc app=leetcode.cn id=1883 lang=python3
#
# [1883] 准时抵达会议现场的最小跳过休息次数
#
from sbw import *


# @lc code=start
from fractions import Fraction
class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        # presums = list(accumulate(dist, initial=0))

        if sum(dist) > hoursBefore * speed:
            return -1
        N = len(dist)
        @cache
        def dfs(i,j):
            if j<0:
                return 0
            res=((dfs(i,j-1) + dist[j]-1)//speed+1)*speed
            if i:
                res=min(res,dfs(i-1,j-1)+dist[j])
            return res
        
        for i in range(N):
            if dfs(i,N-2)+dist[-1]<=speed*hoursBefore:
                return i
        
        # f=[[float('inf')]*N for _ in range(N)]
        f=[0]*N
        for i in range(N):
            pre=0
            for j,d in enumerate(dist[:-1]):
                temp=f[j+1]
                f[j+1]=(f[j]+d+speed-1)//speed*speed
                if i:
                    f[j+1]=min(f[j+1],pre+d)
                pre=temp
            if f[-1]+dist[-1]<=hoursBefore*speed:
                return i



# @lc code=end
assert Solution().minSkips(dist=[1, 3, 2], speed=4, hoursBefore=2) == 1
assert Solution().minSkips(dist = [7,3,5,5], speed = 1, hoursBefore = 10) == -1
assert Solution().minSkips(dist = [7,3,5,5], speed = 2, hoursBefore = 10) == 2
