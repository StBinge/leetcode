#
# @lc app=leetcode.cn id=1599 lang=python3
#
# [1599] 经营摩天轮的最大利润
#
from sbw import *


# @lc code=start
class Solution:
    def minOperationsMaxProfit(
        self, customers: List[int], boardingCost: int, runningCost: int
    ) -> int:
        per_round_profit=4*boardingCost-runningCost
        if per_round_profit<=0:
            return -1
        peoples = 0
        profit = 0
        max_profit=0
        ret=-1
        round=0
        for cust in customers:
            round+=1
            peoples += cust
            board = min(peoples, 4)
            peoples -= board
            profit += board * boardingCost - runningCost
            if profit>max_profit:
                max_profit=profit
                ret=round

        full_rounds=peoples//4
        profit+=full_rounds*per_round_profit
        round+=full_rounds
        if profit>max_profit:
            ret=round

        remain=peoples%4
        profit=remain*boardingCost-runningCost
        if profit>0:
            ret+=1
        return ret



# @lc code=end
assert (
    Solution().minOperationsMaxProfit(
        customers=[10, 9, 6], boardingCost=6, runningCost=4
    )
    == 7
)
assert (
    Solution().minOperationsMaxProfit([10,10,6,4,7],3,8)
    == 9
)
assert (
    Solution().minOperationsMaxProfit(
        customers=[3, 4, 0, 5, 1], boardingCost=1, runningCost=92
    )
    == -1
)

assert Solution().minOperationsMaxProfit([8, 3], 5, 6) == 3
