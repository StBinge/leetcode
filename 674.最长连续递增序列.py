#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#
from typing import List
# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l=0
        r=1
        ret=1
        while r<(L:=len(nums)):
            while r<L and nums[r]>nums[r-1]:
                r+=1
            ret=max(ret,r-l)
            l=r
            r+=1
        return ret
# @lc code=end
nums = [1,3,5,4,7]
assert Solution().findLengthOfLCIS(nums)==3
nums = [2,2,2,2,2]
assert Solution().findLengthOfLCIS(nums)==1
assert Solution().findLengthOfLCIS([1])==1