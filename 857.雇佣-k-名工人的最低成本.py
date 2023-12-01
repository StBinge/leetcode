#
# @lc app=leetcode.cn id=857 lang=python3
#
# [857] 雇佣 K 名工人的最低成本
#
from typing import List
# @lc code=start
import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        q_w=sorted(zip(quality,wage),key=lambda x:x[1]/x[0])
        total_q=0
        ans=float('inf')
        h=[]
        for i in range(k-1):
            total_q+=q_w[i][0]
            heapq.heappush(h,-q_w[i][0])
        for i in  range(k-1,len(quality)):
            q,w=q_w[i]
            total_q+=q
            ans=min(ans,total_q*w/q)
            total_q+=heapq.heappushpop(h,-q)
        return ans
# @lc code=end

