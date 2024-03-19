#
# @lc app=leetcode.cn id=1425 lang=python3
#
# [1425] 带限制的子序列和
#
from sbw import *
# @lc code=start
import heapq
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        L=len(nums)
        # ret=float('-inf')
        # f=[[0]*(k+1) for _ in range()]
        # f=[float('-inf')]*L
        ret=nums[0]
        stack=deque([[nums[0],0]])
        for i in range(1,L):
            while i-stack[0][1]>k:
                stack.popleft()
            cur=max(nums[i],nums[i]+stack[0][0])
            ret=max(ret,cur)
            while stack and cur>=stack[-1][0]:
                stack.pop()
            stack.append([cur,i])

        return ret
# @lc code=end
assert Solution().constrainedSubsetSum(nums = [10,-2,-10,-5,20], k = 2)==23
assert Solution().constrainedSubsetSum(nums = [-1,-2,-3], k = 1)==-1
assert Solution().constrainedSubsetSum(nums = [10,2,-10,5,20], k = 2)==37
