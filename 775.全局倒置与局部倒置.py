#
# @lc app=leetcode.cn id=775 lang=python3
#
# [775] 全局倒置与局部倒置
#
from typing import List
# @lc code=start
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
 
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[i]-i)<=1:
                continue
            else:
                return False
        return True

# @lc code=end
nums = [1,0,2]
assert Solution().isIdealPermutation(nums)
nums = [1,2,0]
assert Solution().isIdealPermutation(nums)==False
