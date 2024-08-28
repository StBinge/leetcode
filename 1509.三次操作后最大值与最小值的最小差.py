#
# @lc app=leetcode.cn id=1509 lang=python3
#
# [1509] 三次操作后最大值与最小值的最小差
#
from sbw import *
# @lc code=start
import heapq
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        L=len(nums)
        if L<5:
            return 0
        if L<9:
            nums.sort()
            gap=L-4
        else:
            min_heap=[]
            max_heap=[]
            for n in nums:
                heapq.heappush(min_heap,n)
                heapq.heappush(max_heap,-n)
                if len(min_heap)>4:
                    heapq.heappop(min_heap)
                if len(max_heap)>4:
                    heapq.heappop(max_heap)
            nums=sorted(min_heap+[-n for n in max_heap])
            gap=4
            L=8
        return min(nums[i+gap]-nums[i] for i in range(L-gap))
# @lc code=end

assert Solution().minDifference([20,66,68,57,45,18,42,34,37,58])==31
assert Solution().minDifference([6,6,0,1,1,4,6])==2
assert Solution().minDifference([3,100,20])==0
assert Solution().minDifference([1,5,0,10,14])==1
assert Solution().minDifference([5,3,2,4])==0