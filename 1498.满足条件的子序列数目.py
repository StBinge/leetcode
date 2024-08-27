#
# @lc app=leetcode.cn id=1498 lang=python3
#
# [1498] 满足条件的子序列数目
#
from sbw import *


# @lc code=start
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mods = 10**9 + 7
        n = len(nums)
        powers = [0] * n
        powers[0] = 1
        for i in range(1, n):
            powers[i] = (powers[i - 1] << 1) % mods
        ret = 0
        p = n
        for i, x in enumerate(nums):
            if x * 2 > target:
                break
            ma = target - x
            p = bisect_right(nums, ma, hi=min(p + 1, n)) - 1
            contribute = powers[p - i] if p >= i else 0
            ret += contribute
        return ret % mods


# @lc code=end
assert Solution().numSubseq(nums=[2, 3, 3, 4, 6, 7], target=12) == 61
assert Solution().numSubseq(nums=[3, 3, 6, 8], target=10) == 6
assert Solution().numSubseq(nums=[3, 5, 6, 7], target=9) == 4
