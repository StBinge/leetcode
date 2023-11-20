#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#
from typing import List
# @lc code=start
from functools import lru_cache
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total=sum(nums)
        if total%k:
            return False
        avg=total//k
        nums.sort()
        if nums[-1]>avg:
            return False
        L=len(nums)
        dp=[False]*(1<<L)
        dp[0]=True
        cur_sum=[0]*(1<<L)
        for mask in range(1<<L):
            if not dp[mask]:
                continue
            for j in range(L):
                if cur_sum[mask]+nums[j]>avg:
                    break
                if mask & (1<<j):
                    continue
                next=mask | 1<<j
                if not dp[next]:
                    cur_sum[next]=(cur_sum[mask]+nums[j])%avg
                    dp[next]=True
        return dp[-1]

# @lc code=end
nums=[2,2,2,2,3,4,5]
k=4
assert Solution().canPartitionKSubsets(nums,k)==False

nums=[1,1,1,1,2,2,2,2]
k=2
assert Solution().canPartitionKSubsets(nums,k)

nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
assert Solution().canPartitionKSubsets(nums,k)
nums = [1,2,3,4]
k = 3
assert Solution().canPartitionKSubsets(nums,k)==False
