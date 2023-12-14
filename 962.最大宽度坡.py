#
# @lc app=leetcode.cn id=962 lang=python3
#
# [962] 最大宽度坡
#
from sbw import *

# @lc code=start
import bisect


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ret=0
        L=len(nums)
        canidates=[[nums[-1],L-1]]
        for i in range(L-2,-1,-1):
            idx=bisect.bisect_left(canidates,[nums[i],])
            if idx<len(canidates):
                ret=max(ret,canidates[idx][1]-i)
            else:
                canidates.append([nums[i],i])
        return ret


# @lc code=end
assert Solution().maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]) == 7
assert Solution().maxWidthRamp([6, 0, 8, 2, 1, 5]) == 4
