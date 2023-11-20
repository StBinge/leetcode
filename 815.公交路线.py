#
# @lc app=leetcode.cn id=815 lang=python3
#
# [815] 公交路线
#
from typing import List
# @lc code=start
from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        graph={}
        L=len(routes)
        stop2bus={}

        for i,route in enumerate(routes):
            for site in route:
                bus_set=stop2bus.setdefault(site,set())
                for b in bus_set:
                    graph.setdefault(i,set()).add(b)
                    graph.setdefault(b,set()).add(i)
                stop2bus[site].add(i)
        s_bus=stop2bus.get(source,None)
        t_bus=stop2bus.get(target,None)
        if not s_bus or not t_bus:
            return -1
        if s_bus & t_bus:
            return 1
        dis=[-1]*L
        for b in s_bus:
            dis[b]=1
        queue=deque(s_bus)
        while queue:
            b=queue.popleft()
            for nxt in graph.get(b,[]):
                if dis[nxt]==-1:
                    dis[nxt]=dis[b]+1
                    queue.append(nxt)
        ret=1000
        for b in t_bus:
            if dis[b]>0:
                ret=min(ret,dis[b])
        return ret if ret!=1000 else -1

# @lc code=end
routes = [[1,2,7],[3,6,7]]
source = 1
target = 6
assert Solution().numBusesToDestination(routes,source,target)==2
routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]] 
source = 15
target = 12
assert Solution().numBusesToDestination(routes,source,target)==-1
