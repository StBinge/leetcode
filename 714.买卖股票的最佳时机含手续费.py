#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        L=len(prices)
        buy=prices[0]+fee
        profit=0
        for i in range(1,L):
            if fee+prices[i]<buy:
                buy=fee+prices[i]
            elif prices[i]>buy:
                profit+=prices[i]-buy
                buy=prices[i]
        return profit

# @lc code=end
prices=[9,8,7,1,2]
fee=3
assert Solution().maxProfit(prices,fee)==0

prices = [1, 3, 2, 8, 4, 9]
fee = 2
assert Solution().maxProfit(prices,fee)==8

prices = [1,3,7,5,10,3]
fee = 3
assert Solution().maxProfit(prices,fee)==6