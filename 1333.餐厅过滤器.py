#
# @lc app=leetcode.cn id=1333 lang=python3
#
# [1333] 餐厅过滤器
#
from sbw import *
# @lc code=start
import heapq
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        heap=[]
        for idx,rat,vf,p,d in restaurants:
            if (veganFriendly>vf) or p>maxPrice or d>maxDistance:
                continue
            heapq.heappush(heap,[-rat,-idx])
        ret=[]
        while heap:
            ret.append(-heapq.heappop(heap)[1])
        return ret
# @lc code=end
assert Solution().filterRestaurants(restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 30, maxDistance = 3)==[4,5]
assert Solution().filterRestaurants(restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 50, maxDistance = 10)==[4,3,2,1,5]
assert Solution().filterRestaurants(restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 1, maxPrice = 50, maxDistance = 10)==[3,1,5]
