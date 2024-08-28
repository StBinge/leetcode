#
# @lc app=leetcode.cn id=1827 lang=python3
#
# [1827] 最少操作使数组递增
#
from sbw import *


# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        pre = 0
        ret = 0
        for n in nums:
            pre=max(pre+1,n)
            ret+=pre-n
        return ret


# @lc code=end
assert Solution().minOperations([1,5,2,4,1]) == 14
assert Solution().minOperations([1, 1, 1]) == 3
