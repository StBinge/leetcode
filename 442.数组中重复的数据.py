#
# @lc app=leetcode.cn id=442 lang=python3
#
# [442] 数组中重复的数据
#
from typing import List
# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret=[]
        for i in range(len(nums)):
            n=abs(nums[i])
            if nums[n-1]<0:
                ret.append(n)
            else:
                nums[n-1]=-nums[n-1]
            
        return ret
# @lc code=end
assert Solution().findDuplicates([4,3,2,7,8,2,3,1])==[2,3]
assert Solution().findDuplicates([1,1,2])==[1]
assert Solution().findDuplicates([1])==[]
