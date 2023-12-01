#
# @lc app=leetcode.cn id=871 lang=python3
#
# [871] 最低加油次数
#
from typing import List
# @lc code=start
import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target,0])
        n=len(stations)
        fuels=[]
        cur_fuel=startFuel
        cur_pos=0
        idx=0
        ret=0

        while cur_fuel>=0 or fuels:
            if idx==n:
                return ret
            pos,fuel=stations[idx]
            dis=pos-cur_pos
            cur_fuel-=dis
            cur_pos=pos

            while cur_fuel<0 and fuels:
                cur_fuel+=-heapq.heappop(fuels)
                ret+=1

            if cur_fuel<0:
                return -1
            
            heapq.heappush(fuels,-fuel)

            idx+=1
# @lc code=end
target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]
assert Solution().minRefuelStops(target,startFuel,stations)==2

target = 100
startFuel = 1
stations = [[10,100]]
assert Solution().minRefuelStops(target,startFuel,stations)==-1

target = 1
startFuel = 1
stations = []
assert Solution().minRefuelStops(target,startFuel,stations)==0