#
# @lc app=leetcode.cn id=1829 lang=python3
#
# [1829] 每个查询的最大异或值
#
from sbw import *
# @lc code=start
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        N=len(nums)
        xor=0
        ret=[0]*N
        Mask=(1<<maximumBit)-1
        for i in range(N):
            xor^=nums[i]
            ret[-1-i]=xor^Mask
        return ret
# @lc code=end  
assert Solution().getMaximumXor(nums = [2,3,4,7], maximumBit = 3)==[5,2,6,5]
assert Solution().getMaximumXor(nums = [0,1,2,2,5,7], maximumBit = 3)==[4,3,6,4,6,7]
assert Solution().getMaximumXor(nums = [0,1,1,3], maximumBit = 2)==[0,3,2,3]
