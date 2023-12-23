#
# @lc app=leetcode.cn id=910 lang=python3
#
# [910] 最小差值 II
#
import enum

from sympy import false
from sbw import *
# @lc code=start
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=nums[-1]-nums[0]
        if ans==0:
            return 0
        up=nums[-1]-k
        down=nums[0]+k
        for i in range(len(nums)-1):
            ans=min(ans,max(up,nums[i]+k)-min(down,nums[i+1]-k))
        return ans


# @lc code=end
nums = [0,10]
k = 2
assert Solution().smallestRangeII(nums,k)==6

nums = [1]
k = 0
assert Solution().smallestRangeII(nums,k)==0
