#
# @lc app=leetcode.cn id=1518 lang=python3
#
# [1518] 换水问题
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cnt=numBottles//(numExchange-1)
        return numBottles+cnt-int(numBottles%(numExchange-1)==0)
# @lc code=end
assert Solution().numWaterBottles(15,4)==19
assert Solution().numWaterBottles(9,3)==13
