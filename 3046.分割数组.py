#
# @lc app=leetcode.cn id=3046 lang=python3
#
# [3046] 分割数组
#
from sbw import *
# @lc code=start
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        return all(v<3 for v in Counter(nums).values())
# @lc code=end
assert Solution().isPossibleToSplit([1,1,1,1])==False
assert Solution().isPossibleToSplit([1,1,2,2,3,4])
