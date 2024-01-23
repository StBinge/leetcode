#
# @lc app=leetcode.cn id=1208 lang=python3
#
# [1208] 尽可能使字符串相等
#
from sbw import *
# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        L=len(s)
        l=0
        cost=0
        ret=0
        dif=[abs(ord(c1)-ord(c2)) for c1,c2 in zip(s,t)]

        for r in range(L):
            cost+=dif[r]
            while cost>maxCost:
                cost-=dif[l]
                l+=1
            ret=max(r-l+1,ret)
        return ret
# @lc code=end
assert Solution().equalSubstring(s = "abcd", t = "acde", maxCost = 0)==1
assert Solution().equalSubstring(s = "abcd", t = "bcdf", maxCost = 3)==3
assert Solution().equalSubstring(s = "abcd", t = "cdef", maxCost = 3)==1
