#
# @lc app=leetcode.cn id=3066 lang=python3
#
# [3066] 超过阈值的最少操作数 II
#
from sbw import *
# @lc code=start
import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap=[]
        ret=0
        for n in nums:
            if n<k:
                heapq.heappush(heap,n)

        while len(heap)>1:
            x,y=heapq.heappop(heap),heapq.heappop(heap)
            z=x*2+y
            if z<k:
                heapq.heappush(heap,z)
            ret+=1
        return ret + len(heap)


# @lc code=end
assert Solution().minOperations([9,98,52,8],98)==2
assert Solution().minOperations([999999999,999999999,999999999],1000000000)==2
assert Solution().minOperations(nums = [1,1,2,4,9], k = 20)==4
assert Solution().minOperations(nums = [2,11,10,1,3], k = 10)==2
