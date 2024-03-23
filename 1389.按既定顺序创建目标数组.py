#
# @lc app=leetcode.cn id=1389 lang=python3
#
# [1389] 按既定顺序创建目标数组
#
from sbw import *
# @lc code=start
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target=[0]*len(nums)
        for i in range(len(nums)):
            idx,n=index[i],nums[i]
            if i==idx:
                target[idx]=n
            else:
                for j in range(i,idx,-1):
                    target[j]=target[j-1]
                target[idx]=n

        return target
# @lc code=end

assert Solution().createTargetArray(nums = [1,2,3,4,0], index = [0,1,2,3,0])==[0,1,2,3,4]
assert Solution().createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1])==[0,4,1,3,2]