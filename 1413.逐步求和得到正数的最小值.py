#
# @lc app=leetcode.cn id=1413 lang=python3
#
# [1413] 逐步求和得到正数的最小值
#
from sbw import *
# @lc code=start
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ret=1
        pre=0
        for n in nums:
            pre+=n
            ret=max(ret,1-pre)
        return ret
# @lc code=end
assert Solution().minStartValue([1,-2,-3])==5
assert Solution().minStartValue(nums = [1,2])==1
assert Solution().minStartValue([-3,2,-3,4,2])==5
