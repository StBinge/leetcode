#
# @lc app=leetcode.cn id=1887 lang=python3
#
# [1887] 使数组元素相等的减少操作次数
#
from sbw import *


# @lc code=start
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        sorted_keys = sorted(counter.keys(),reverse=True)
        ret = 0
        cur = 0
        for k in sorted_keys:
            ret += cur
            cur += counter[k]
        return ret


# @lc code=end
assert Solution().reductionOperations([1,1,2,2,3]) == 4
assert Solution().reductionOperations([1, 1, 1]) == 0
assert Solution().reductionOperations([5, 1, 3]) == 3
