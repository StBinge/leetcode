#
# @lc app=leetcode.cn id=743 lang=python3
#
# [743] 网络延迟时间
#
from typing import List
# @lc code=start
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ret=[float('inf')]*(n+1)
        ret[k]=0
        g=[[float('inf')]*(n+1) for _ in range(n+1)]
        # edges:dict[int,dict[int,int]]={}
        for s,e,t in times:
            g[s][e]=t

        stack=[(0,k)]
        while stack:
            t,x=heapq.heappop(stack)
            if ret[x]<t:
                continue
            for y in range(1,n+1):
                tt=t+g[x][y]
                if tt<ret[y]:
                    ret[y]=tt
                    heapq.heappush(stack,(tt,y))
        res=max(ret[1:])
        return res if res<float('inf') else -1
# @lc code=end
times=[[4,2,76],[1,3,79],[3,1,81],[4,3,30],[2,1,47],[1,5,61],[1,4,99],[3,4,68],[3,5,46],[4,1,6],[5,4,7],[5,3,44],[4,5,19],[2,3,13],[3,2,18],[1,2,0],[5,1,25],[2,5,58],[2,4,77],[5,2,74]]
n=5
k=3
assert Solution().networkDelayTime(times,n,k)==59

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
assert Solution().networkDelayTime(times,n,k)==2
times = [[1,2,1]]
n = 2
k = 1
assert Solution().networkDelayTime(times,n,k)==1

times = [[1,2,1]]
n = 2
k = 2
assert Solution().networkDelayTime(times,n,k)==-1
