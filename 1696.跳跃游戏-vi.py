#
# @lc app=leetcode.cn id=1696 lang=python3
#
# [1696] 跳跃游戏 VI
#
from sbw import *
# @lc code=start
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N=len(nums)
    
        f=nums[0]
        stack=deque([[0,nums[0]]])
        for i in range(1,N):
            while i-stack[0][0]>k:
                stack.popleft()
            f=stack[0][1]+nums[i]
            while stack and stack[-1][1]<=f:
                stack.pop()
            stack.append([i,f])
        return f
# @lc code=end
assert Solution().maxResult(nums = [1,-5,-20,4,-1,3,-6,-3], k = 2)==0
assert Solution().maxResult(nums = [10,-5,-2,4,0,3], k = 3)==17
assert Solution().maxResult(nums = [1,-1,-2,4,-7,3], k = 2)==7
