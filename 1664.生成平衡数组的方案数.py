#
# @lc app=leetcode.cn id=1664 lang=python3
#
# [1664] 生成平衡数组的方案数
#
from sbw import *


# @lc code=start
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        N = len(nums)

        tot_odds = tot_evens = 0
        for i, n in enumerate(nums):
            if i & 1:
                tot_odds += n
            else:
                tot_evens += n
        ret = 0
        pre_odds = pre_evens = 0
        for i in range(N):
            if i & 1:
                right_evens = tot_odds - pre_odds - nums[i]
                right_odds = tot_evens - pre_evens
            else:
                right_evens = tot_odds - pre_odds
                right_odds = tot_evens - pre_evens - nums[i]
            if pre_evens + right_evens == pre_odds + right_odds:
                ret += 1
            if i & 1:
                pre_odds += nums[i]
            else:
                pre_evens += nums[i]

        return ret


# @lc code=end

assert Solution().waysToMakeFair([1]) == 1
assert Solution().waysToMakeFair([1, 2, 3]) == 0
assert Solution().waysToMakeFair([1, 1, 1]) == 3
assert Solution().waysToMakeFair([2, 1, 6, 4]) == 1
