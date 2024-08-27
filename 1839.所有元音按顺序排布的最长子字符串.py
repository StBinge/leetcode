#
# @lc app=leetcode.cn id=1839 lang=python3
#
# [1839] 所有元音按顺序排布的最长子字符串
#
from sbw import *


# @lc code=start
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:

        N = len(word)
        idx = 0
        vows = "aeiou"
        ret = 0
        start = 0
        while idx<N:
            while idx < N and word[idx] != "a":
                idx += 1
            start = idx
            idx += 1
            nxt = 1
            while idx < N:
                nxt_ch = word[idx]
                if nxt_ch == word[idx - 1]:
                    idx += 1
                    continue
                else:
                    if nxt == 5:
                        ret = max(ret, idx - start)
                        break
                    if nxt_ch == vows[nxt]:
                        nxt += 1
                        idx += 1
                    else:
                        break
        if nxt == 5:
            ret = max(ret, N - start)
        return ret


# @lc code=end
assert Solution().longestBeautifulSubstring("aiaeioouaaeeiouuiuieeo") == 8
assert Solution().longestBeautifulSubstring("aeeeiiiioooauuuaeiou") == 5
assert Solution().longestBeautifulSubstring("aeiaaioaaaaeiiiiouuuooaauuaeiu") == 13
