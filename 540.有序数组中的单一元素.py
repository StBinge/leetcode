#
# @lc app=leetcode.cn id=540 lang=python3
#
# [540] 有序数组中的单一元素
#
from typing import List
# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]==nums[mid^1]:
                left=mid+1
            else:
                right=mid
        return nums[left]
# @lc code=end

assert Solution().singleNonDuplicate([3,3,7,7,10,11,11])==10
assert Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8])==2