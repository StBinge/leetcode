#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#
from typing import List
# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # N=len(nums)
        dp=[0]*(target+1)
        dp[0]=1
        for i in range(1,target+1):
            for n in nums:
                if i-n>=0:
                    dp[i]+=dp[i-n]
        return dp[-1]


# @lc code=end

assert Solution().combinationSum4([1,2,3],4)==7
assert Solution().combinationSum4([9],3)==0