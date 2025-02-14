#
# @lc app=leetcode.cn id=2311 lang=python3
# @lcpr version=30204
#
# [2311] 小于等于 K 的最长二进制子序列
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        N = len(s)
        M = k.bit_length()
        if N < M:
            return N

        ret = M if int(s[-M:], 2) <= k else M - 1
        return ret + s[:-M].count("0")


# @lc code=end
assert Solution().longestSubsequence("00101001", 1) == 6
assert Solution().longestSubsequence("1001010", 5) == 5


#
# @lcpr case=start
# "1001010"\n5\n
# @lcpr case=end

# @lcpr case=start
# "00101001"\n1\n
# @lcpr case=end

#
