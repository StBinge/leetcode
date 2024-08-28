#
# @lc app=leetcode.cn id=1575 lang=python3
#
# [1575] 统计所有可行路径
#
from sbw import *
# @lc code=start
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        Mod=10**9+7
        start_pos=locations[start]
        finish_pos=locations[finish]
        locations.sort()
        start=bisect_left(locations,start_pos)
        finish=bisect_left(locations,finish_pos)
        N=len(locations)
        
        fl=[[0]*(fuel+1) for _ in range(N)]
        fr=[[0]*(fuel+1) for _ in range(N)]
        fl[start][0]=1
        fr[start][0]=1

        for f in range(1,fuel+1):
            for c in range(N-2,-1,-1):
                delta=locations[c+1]-locations[c]
                if delta<=f:
                    fl[c][f]=fr[c+1][f-delta]+(2*fl[c+1][f-delta] if f>delta else 0)
                    fl[c][f]%=Mod
            
            for c in range(1,N):
                delta=locations[c]-locations[c-1]
                if delta<=f:
                    fr[c][f]=fl[c-1][f-delta]+(2*fr[c-1][f-delta] if f>delta else 0)
                    fr[c][f]%=Mod
        ret=sum(fl[finish])+sum(fr[finish])
        if finish==start:
            ret-=1
        return ret%Mod
# @lc code=end

assert Solution().countRoutes([15,17,12,8,18],4,1,1)==1
assert Solution().countRoutes(locations = [5,2,1], start = 0, finish = 2, fuel = 3)==0
assert Solution().countRoutes(locations = [4,3,1], start = 1, finish = 0, fuel = 6)==5
assert Solution().countRoutes(locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5)==4