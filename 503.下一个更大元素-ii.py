#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#
from typing import List
# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        L=len(nums)
        stack=[]
        ret=[-1]*L
        for i in range(2*L-1):
            while stack and nums[stack[-1]%L]<nums[i%L]:
                ret[stack.pop()%L]=nums[i%L]
            stack.append(i)
        return ret
            
# @lc code=end

assert Solution().nextGreaterElements([1])==[-1]
assert Solution().nextGreaterElements([1,2,1])==[2,-1,2]
assert Solution().nextGreaterElements([1,2,3,4,3])==[2,3,4,-1,4]