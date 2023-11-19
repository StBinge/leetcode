#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#
from typing import List
# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            n=abs(n)
            if nums[n-1]>0:
                nums[n-1]=-nums[n-1]
        
        ret=[]
        for i in range(len(nums)):
            if nums[i]>0:
                ret.append(i+1)
        return ret
# @lc code=end
assert Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])==[5,6]
assert Solution().findDisappearedNumbers([1,1])==[2]
