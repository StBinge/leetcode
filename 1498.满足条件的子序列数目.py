#
# @lc app=leetcode.cn id=1498 lang=python3
#
# [1498] 满足条件的子序列数目
#
from sbw import *
# @lc code=start
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        if nums[0]*2>target:
            return 0
        L=len(nums)
        l=0
        r=L-1
        ret=0
        Mods=10**9+7
        while l<=r:
            if nums[l]+nums[r]<=target:
                ret=(ret+pow(2,r-l))%Mods
                l+=1
            else:
                r-=1
        return ret
# @lc code=end
assert Solution().numSubseq(nums = [2,3,3,4,6,7], target = 12)==61
assert Solution().numSubseq(nums = [3,3,6,8], target = 10)==6
assert Solution().numSubseq(nums = [3,5,6,7], target = 9)==4
