#
# @lc app=leetcode.cn id=1094 lang=python3
#
# [1094] 拼车
#
from sbw import *
# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops=defaultdict(int)
        for num,start,end in trips:
            stops[start]+=num
            stops[end]-=num
        cnt=0
        for stop in sorted(stops.keys()):
            cnt+=stops[stop]
            if cnt>capacity:
                return False
        return True
# @lc code=end
assert Solution().carPooling(trips = [[2,1,5],[3,3,7]], capacity = 5)==True
assert Solution().carPooling(trips = [[2,1,5],[3,3,7]], capacity = 4)==False
