#
# @lc app=leetcode.cn id=446 lang=python3
#
# [446] 等差数列划分 II - 子序列
#
from typing import List
# @lc code=start
from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        L=len(nums)
        ans=0
        dp=[defaultdict(int) for _ in range(L)]
        for i in range(L):
            for j in range(i):
                diff=nums[i]-nums[j]
                cnt=dp[j][diff]
                ans+=cnt
                dp[i][diff]+=cnt+1
        return ans

# @lc code=end
assert Solution().numberOfArithmeticSlices([2,4,6,8,10])==7
assert Solution().numberOfArithmeticSlices([7,7,7,7,7])==16
