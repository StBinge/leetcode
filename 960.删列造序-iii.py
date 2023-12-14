#
# @lc app=leetcode.cn id=960 lang=python3
#
# [960] 删列造序 III
#
from sbw import *


# @lc code=start
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        W = len(strs[0])
        R = len(strs)
        dp = [1] * W
        for w in range(W - 2, -1, -1):
            for nw in range(w + 1, W):
                if all(word[w] <= word[nw] for word in strs):
                    dp[w] = max(dp[w], dp[nw] + 1)
        return W - max(dp)


# @lc code=end
strs = ["ghi","def","abc"]
assert Solution().minDeletionSize(strs) == 0
strs = ["edcba"]
assert Solution().minDeletionSize(strs) == 4

strs = ["babca", "bbazb"]
assert Solution().minDeletionSize(strs) == 3
