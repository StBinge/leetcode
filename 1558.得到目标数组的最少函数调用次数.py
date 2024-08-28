#
# @lc app=leetcode.cn id=1558 lang=python3
#
# [1558] 得到目标数组的最少函数调用次数
#
from sbw import *


# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ret = 0
        ma = 0
        for n in nums:
            ret += n.bit_count()
            ma = max(ma, n)
        return ret + (ma >> 1).bit_length()


# @lc code=end
assert Solution().minOperations([7,4,3,2,0,2]) == 10
assert Solution().minOperations([2, 4, 8, 16]) == 8
assert Solution().minOperations([0]) == 0
assert Solution().minOperations([3, 2, 2, 4]) == 7
assert Solution().minOperations([4, 2, 5]) == 6
