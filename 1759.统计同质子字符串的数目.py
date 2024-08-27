#
# @lc app=leetcode.cn id=1759 lang=python3
#
# [1759] 统计同质子字符串的数目
#

from sbw import *


# @lc code=start
class Solution:
    def countHomogenous(self, s: str) -> int:
        ret = 0
        Mod = 10**9 + 7
        for k, g in groupby(s):
            cnt = len(list(g))
            ret += cnt * (cnt + 1) // 2
        return ret % Mod


# @lc code=end
assert Solution().countHomogenous("zzzzz") == 15
assert Solution().countHomogenous("xy") == 2
assert Solution().countHomogenous("abbcccaa") == 13
