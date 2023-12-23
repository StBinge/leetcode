#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#
from sbw import *
# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l,r=0,len(nums)-1
        while l<r:
            while l<r and nums[l]%2==0:
                l+=1
            while l<r and nums[r]%2:
                r-=1
            if l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        return nums
# @lc code=end

