#
# @lc app=leetcode.cn id=456 lang=python3
#
# [456] 132 模式
#
from typing import List
# @lc code=start
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N=len(nums)
        if len(nums)<3:
            return False

        left_most=[10**10]
        stack=[]
        for i in range(N):
            while stack and nums[i]>=nums[stack[-1]]:
                stack.pop()
            if stack and left_most[stack[-1]]<nums[i]:
                return True
            stack.append(i)
            left_most.append(min(left_most[-1],nums[i]))
        return False
# @lc code=end

assert Solution().find132pattern([1,3,2,4,5,6,7,8,9,10])==True
assert Solution().find132pattern([3,1,4,2])==True
assert Solution().find132pattern([1,0,1,-4,-3])==False
assert Solution().find132pattern([1,2,3,4])==False
assert Solution().find132pattern([-1,3,2,0])==True
assert Solution().find132pattern([3,5,0,3,4])