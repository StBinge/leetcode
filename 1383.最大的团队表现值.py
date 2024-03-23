#
# @lc app=leetcode.cn id=1383 lang=python3
#
# [1383] 最大的团队表现值
#
from sbw import *
# @lc code=start
import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        employees=sorted(zip(efficiency,speed),key=lambda x:-x[0])
        q=[]
        tot,ret=0,0
        for i in range(n):
            e,s=employees[i]
            tot+=s
            ret=max(ret,e*tot)
            heapq.heappush(q,s)
            if len(q)==k:
                tot-=heapq.heappop(q)
        return ret % (10**9+7)

# @lc code=end
assert Solution().maxPerformance(3,[2,8,2],[2,7,1],2)==56
assert Solution().maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2)==60
