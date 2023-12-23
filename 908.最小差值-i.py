#
# @lc app=leetcode.cn id=908 lang=python3
#
# [908] 最小差值 I
#
from sbw import *
# @lc code=start
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        Min=min(nums)
        Max=max(nums)
        return max(Max-Min-2*k,0)
# @lc code=end
assert Solution().smallestRangeI([1,3,6],3)==0
assert Solution().smallestRangeI([0,10],2)==6
assert Solution().smallestRangeI([1],0)==0
