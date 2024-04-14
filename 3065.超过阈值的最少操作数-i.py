#
# @lc app=leetcode.cn id=3065 lang=python3
#
# [3065] 超过阈值的最少操作数 I
#
from sbw import *
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(n<k for n in nums)
# @lc code=end
assert Solution().minOperations(nums = [1,1,2,4,9], k = 9)==4
