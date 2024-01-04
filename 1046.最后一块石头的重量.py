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
        cur=heapq.heappop(heap)
        while len(heap):
            nxt=heapq.heappop(heap)
            cur=cur-nxt
            if heap and cur>heap[0]:
                cur=heapq.heappushpop(heap,cur)
        return -cur
# @lc code=end
assert Solution().lastStoneWeight([7,6,7,6,9])==3
assert Solution().lastStoneWeight([2,7,4,1,8,1])==1