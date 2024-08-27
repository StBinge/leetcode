#
# @lc app=leetcode.cn id=1540 lang=python3
#
# [1540] K 次操作转变字符串
#
from sbw import *


# @lc code=start
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        cnt=[0]*26
        for c1, c2 in zip(s, t):
            if c1 == c2:
                continue
            code1 = ord(c1)
            code2 = ord(c2)
            op = (code2 - code1) % 26
            cnt[op]+=1
        for i,c in enumerate(cnt):
            if i+26*(c-1)>k:
                return False


        return True


# @lc code=end
assert Solution().canConvertString(s="aab", t="bbb", k=27)
assert Solution().canConvertString(s="abc", t="bcd", k=10) == False
assert Solution().canConvertString("input", "ouput", 9)
