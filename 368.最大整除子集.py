#
# @lc app=leetcode.cn id=368 lang=python3
#
# [368] 最大整除子集
#
from typing import *
# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        L=len(nums)
        nums.sort()
        max_cnt=1
        max_val=nums[0]
        dp=[1]*L
        for i in range(1,L):
            for j in range(i):
                if nums[i]%nums[j]==0:
                    dp[i]=max(dp[j]+1,dp[i])
            if dp[i]>max_cnt:
                max_cnt=dp[i]
                max_val=nums[i]
        if max_cnt==1:
            return [nums[0]]
        ret=[]
        for i in range(L-1,-1,-1):
            if dp[i]==max_cnt and max_val % nums[i]==0:
                ret.append(nums[i])
                max_val=nums[i]
                max_cnt-=1
            if max_cnt==0:
                break
        return ret[::-1]
# @lc code=end
print(Solution().largestDivisibleSubset([1,2,3]))
print(Solution().largestDivisibleSubset([1,2,4,8]))
