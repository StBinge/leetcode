#
# @lc app=leetcode.cn id=1018 lang=python3
#
# [1018] 可被 5 整除的二进制前缀
#
from sbw import *


# @lc code=start
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = 0
        ret = [False] * len(nums)
        for i, bit in enumerate(nums):
            n = (n << 1) + bit
            if n % 5 == 0:
                ret[i] = True
        return ret


# @lc code=end
nums = [1, 1, 1]
ret = "[false,false,false]"
assert Solution().prefixesDivBy5(nums) == eval_list_str(ret)

nums = [0, 1, 1]
ret = "[true,false,false]"
assert Solution().prefixesDivBy5(nums) == eval_list_str(ret)
