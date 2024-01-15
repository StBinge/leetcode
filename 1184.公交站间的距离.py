#
# @lc app=leetcode.cn id=1184 lang=python3
#
# [1184] 公交站间的距离
#
from sbw import *
# @lc code=start
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start>destination:
            start,destination=destination,start
        
        return min(sum(distance[start:destination]),sum(distance[:start])+sum(distance[destination:]))
# @lc code=end
assert Solution().distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 3 )==4
assert Solution().distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 1 )==1
