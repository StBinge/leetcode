#
# @lc app=leetcode.cn id=945 lang=python3
#
# [945] 使数组唯一的最小增量
#
from sbw import *
# @lc code=start
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        nums.append(1000000)
        taken=0
        ret=0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                taken+=1
                ret-=nums[i]
                continue
            fill=min(taken,nums[i]-nums[i-1]-1)
            ret+=fill*(fill+1)//2+fill*nums[i-1]
            taken-=fill
        return ret



        
# @lc code=end
nums = [3,2,1,2,1,7]
assert Solution().minIncrementForUnique(nums)==6

nums = [1,2,2]
assert Solution().minIncrementForUnique(nums)==1
