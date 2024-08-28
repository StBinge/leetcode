#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#
from sbw import *
# @lc code=start
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd=1
        for i in range(0,len(nums),2):
            if nums[i]%2==1:
                while nums[odd]%2:
                    odd+=2
                nums[i],nums[odd]=nums[odd],nums[i]
        
        
        return nums
# @lc code=end
assert Solution().sortArrayByParityII([4,2,5,7])==[4,5,2,7]
