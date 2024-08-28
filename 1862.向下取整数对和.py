#
# @lc app=leetcode.cn id=1862 lang=python3
#
# [1862] 向下取整数对和
#
from sbw import *


# @lc code=start
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        mx = max(nums)
        cnt = [0] * (mx + 1)
        for n in nums:
            cnt[n] += 1
        presums = list(accumulate(cnt, initial=0))

        ret = 0
        Mod = 10**9 + 7
        for y in range(1, mx + 1):
            if not cnt[y]:
                continue
            d = 1
            while d * y <= mx:
                ret += (presums[min((d + 1) * y,mx+1)] - presums[d * y]) * d*cnt[y]
                ret %= Mod
                d += 1
        return ret


# @lc code=end
assert Solution().sumOfFlooredPairs(nums=[2, 5, 9]) == 10
