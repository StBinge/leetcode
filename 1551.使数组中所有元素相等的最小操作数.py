#
# @lc app=leetcode.cn id=1551 lang=python3
#
# [1551] 使数组中所有元素相等的最小操作数
#


# @lc code=start
class Solution:
    def minOperations(self, n: int) -> int:
        return n * n // 4


# @lc code=end

assert Solution().minOperations(6) == 9
assert Solution().minOperations(3) == 2
