#
# @lc app=leetcode.cn id=502 lang=python3
#
# [502] IPO
#
from typing import List
# @lc code=start
import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w>=max(capital):
            return w+sum(sorted(profits,reverse=True)[:k])
        
        L=len(capital)
        cost_profit=sorted(zip(capital,profits),key=lambda x:x[0])
        idx=0
        most=[]
        while k:
            while idx<L and w>=cost_profit[idx][0]:
                heapq.heappush(most,-cost_profit[idx][1])
                idx+=1
            if not most:
                return w
            w-=heapq.heappop(most)
            k-=1
        return w
            
# @lc code=end
assert Solution().findMaximizedCapital(1,0,[1,2,3],[1,1,2])==0

k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]
assert Solution().findMaximizedCapital(k,w,profits,capital)==4

assert Solution().findMaximizedCapital(3,w,profits,[0,1,2])==6