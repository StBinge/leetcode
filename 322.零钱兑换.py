#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
from typing import List
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[10**9] * (amount+1)
        dp[0]=0

        for coin in coins:
            for sum in range(coin,amount+1):
                dp[sum]=min(dp[sum],dp[sum-coin]+1)
        return dp[-1] if dp[-1]!=10**9 else -1
# @lc code=end

assert Solution().coinChange([186,419,83,408],6249)==20
assert Solution().coinChange([1,2,5],11)==3
assert Solution().coinChange([2],3)==-1
assert Solution().coinChange([1],0)==0