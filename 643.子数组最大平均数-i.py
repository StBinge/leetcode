#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#
from typing import List
# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=sum(nums[:k])
        ret=s
        for i in range(k,len(nums)):
            s+=nums[i]-nums[i-k]
            ret=max(ret,s)
        return ret/k

# @lc code=end
nums = [0,0,3,2,4]
k = 5
assert Solution().findMaxAverage(nums,k)==1.8

nums = [1,12,-5,-6,50,3]
k = 4
assert Solution().findMaxAverage(nums,k)==12.75
