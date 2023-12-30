#
# @lc app=leetcode.cn id=983 lang=python3
#
# [983] 最低票价
#
from sbw import *
# @lc code=start
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        Max=max(days)
        f=[0]*(Max+1)
        vis=set(days)
        for d in range(Max+1):
            if d not in vis:
                f[d]=f[d-1]
                continue
            f[d]=min(f[d-1]+costs[0],f[max(d-7,0)]+costs[1],f[max(d-30,0)]+costs[2])
            # f[d]=f[d-1]+costs[0]
            # if d>=7:
            #     f[d]=min(f[d],f[d-7]+costs[1])
            # if d>=30:
            #     f[d]=min(f[d],f[d-30]+costs[2])
        return f[-1]
# @lc code=end
days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]
assert Solution().mincostTickets(days,costs)==17

days = [1,4,6,7,8,20]
costs = [2,7,15]
assert Solution().mincostTickets(days,costs)==11
