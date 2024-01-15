#
# @lc app=leetcode.cn id=1109 lang=python3
#
# [1109] 航班预订统计
#
from sbw import *
# @lc code=start
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        counter=[0]*(n+1)
        for s,e,c in bookings:
            counter[s-1]+=c
            counter[e]-=c
        ret=[0]*n
        s=0
        for i in range(n):
            s+=counter[i]
            ret[i]=s
        return ret
# @lc code=end
assert Solution().corpFlightBookings(bookings = [[1,2,10],[2,2,15]], n = 2)==[10,25]
assert Solution().corpFlightBookings(bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5)==[10,55,45,25,25]
