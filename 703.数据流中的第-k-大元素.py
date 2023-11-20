#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第 K 大元素
#
from typing import List
# @lc code=start
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.heap=[]
        # if not len(nums):
        #     nums.append(-10**5)
        for n in nums:
            if len(self.heap)<k:
                heapq.heappush(self.heap,n)
            elif self.heap[0]>=n:
                continue
            else:
                heapq.heappushpop(self.heap,n)
    # def __insert(self,val):
    #     if len(self.heap)<self.k:
    #         heapq.heappop(self.heap,val)
    #     elif self.heap[0]>val:
    #         return self.heap[0]
    #     else:
    #         heapq.heappushpop(self.heap,n)

    def add(self, val: int) -> int:
        if len(self.heap)<self.k:
            heapq.heappush(self.heap,val)
            return self.heap[0]
        if val<=self.heap[0]:
            return self.heap[0]
        heapq.heappushpop(self.heap,val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

