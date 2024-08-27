#
# @lc app=leetcode.cn id=1717 lang=python3
#
# [1717] 删除子字符串的最大得分
#
from sbw import *


# @lc code=start
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def cnt(ac: str, bc: str):
            a = b = 0
            ab = 0
            ba = 0
            for c in s:
                if c == ac:
                    a += 1
                elif c == bc:
                    if a:
                        a -= 1
                        ab += 1
                    else:
                        b += 1
                else:
                    ba += min(a, b)
                    a = b = 0
            return ab, ba + min(a, b)

        if x > y:
            ab, ba = cnt("a", "b")
            return ab * x + ba * y
        else:
            ba, ab = cnt("b", "a")
            return ba * y + ab * x


# @lc code=end
assert Solution().maximumGain("cbaabwbbbabbwaaq", 4074, 9819) == 23712
assert Solution().maximumGain(s="aabbaaxybbaabb", x=5, y=4) == 20
assert Solution().maximumGain(s="cdbcbbaaabab", x=4, y=5) == 19
