#
# @lc app=leetcode.cn id=1403 lang=python3
#
# [1403] 非递增顺序的最小子序列
#
from sbw import *
# @lc code=start
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        s=sum(nums)
        pre=0
        for i in range(len(nums)):
            pre+=nums[i]
            if pre*2>s:
                return nums[:i+1]
# @lc code=end
assert Solution().minSubsequence([4,3,10,9,8])==[10,9]
