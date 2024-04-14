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
            return min(nums[i]-nums[i-gap] for i in range(gap,L))

        min_heap=[]
        max_heap=[]
        for n in nums:
            heapq.heappush(min_heap,-n)
            heapq.heappush(max_heap,n)
            if len(min_heap)>4:
                heapq.heappop(min_heap)
            if len(max_heap)>4:
                heapq.heappop(max_heap)
        # mins=sorted(min_heap)
        # maxs=sorted(max_heap)
        # ret=float('inf')
        ar=sorted(max_heap+[-n for n in min_heap])
        return min(ar[i+4]-ar[i] for i in range(4))

# @lc code=end

assert Solution().minDifference([6,6,0,1,1,4,6])==2
assert Solution().minDifference([3,100,20])==0
assert Solution().minDifference([1,5,0,10,14])==1
assert Solution().minDifference([5,3,2,4])==0