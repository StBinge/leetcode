#
# @lc app=leetcode.cn id=1897 lang=python3
#
# [1897] 重新分配字符使所有字符串都相等
#
from sbw import *


# @lc code=start
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        cnt = defaultdict(int)
        for word in words:
            for ch in word:
                cnt[ch] += 1
        N = len(words)
        return all(v % N == 0 for v in cnt.values())


# @lc code=end

assert not Solution().makeEqual(["ab","a"])

