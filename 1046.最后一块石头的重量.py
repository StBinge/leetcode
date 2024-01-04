#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#
from sbw import *
# @lc code=start
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for s in stones:
            heapq.heappush(heap,-s)
        while len(heap)>1:
            cur=-heapq.heappop(heap)
            while heap and cur>=-stones[0]:
                cur+=heapq.heappop(heap)
            if cur>0:
                heapq.heappush(heap,-cur)
        return heap[0]
# @lc code=end

assert Solution().lastStoneWeight([2,7,4,1,8,1])==1