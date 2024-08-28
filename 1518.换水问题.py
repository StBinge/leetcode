#
# @lc app=leetcode.cn id=1518 lang=python3
#
# [1518] 换水问题
#


# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles-1)//(numExchange-1)


# @lc code=end
assert Solution().numWaterBottles(2, 3) == 2
assert Solution().numWaterBottles(15, 4) == 19
assert Solution().numWaterBottles(9, 3) == 13
