#
# @lc app=leetcode.cn id=891 lang=python3
#
# [891] 子序列宽度之和
#
from typing import List
# @lc code=start
import math
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        Mod=10**9+7
        n=len(nums)
        ret=0
        power=1
        for i in range(n):
            add=nums[i]*power
            sub=nums[n-1-i]*power
            ret=(ret+add-sub)%Mod
            power<<=1
        return ret
# @lc code=end
assert Solution().sumSubseqWidths([2,1,3])==6
assert Solution().sumSubseqWidths([2])==0
