#
# @lc app=leetcode.cn id=1611 lang=python3
#
# [1611] 使整数变为 0 的最少操作次数
#


# @lc code=start
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        sign = 1
        for i in range(29, -1, -1):
            if n & (1 << i):
                ans += sign * ((1 << (i + 1)) - 1)
                sign = -sign
        return ans


# @lc code=end
assert Solution().minimumOneBitOperations(333) == 393
assert Solution().minimumOneBitOperations(6) == 4
assert Solution().minimumOneBitOperations(3) == 2
