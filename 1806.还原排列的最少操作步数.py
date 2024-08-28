#
# @lc app=leetcode.cn id=1806 lang=python3
#
# [1806] 还原排列的最少操作步数
#


# @lc code=start
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        idx = 1
        for i in range(n):
            if idx < n // 2:
                idx *= 2
            else:
                idx = (idx - n // 2) * 2 + 1
            if idx == 1:
                return i + 1


# @lc code=end
assert Solution().reinitializePermutation(6) == 4
assert Solution().reinitializePermutation(4) == 2
assert Solution().reinitializePermutation(2) == 1
