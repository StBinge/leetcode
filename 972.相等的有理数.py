#
# @lc app=leetcode.cn id=972 lang=python3
#
# [972] 相等的有理数
#
from sbw import *
# @lc code=start
from fractions import Fraction
class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def parse(s:str):
            dot_idx=s.find('.')
            if dot_idx<0:
                return Fraction(int(s),1)
            ans=Fraction(int(s[:dot_idx]),1)
            s=s[dot_idx+1:]
            if not s:
                return ans
            bracked_idx=s.find('(')
            if bracked_idx<0:
                return ans+Fraction(int(s),10**(len(s)))
            scale=10**bracked_idx
            if bracked_idx>0:
                ans+=Fraction(int(s[:bracked_idx]),scale)
            s=s[bracked_idx+1:-1]
            ans+=Fraction(int(s),scale*(10**(len(s))-1))
            return ans
        return parse(s)==parse(t)
# @lc code=end
s = "0.9(9)"
t = "1."
assert Solution().isRationalEqual(s,t)

s="1.(1)"
t="1.0(1)"
assert Solution().isRationalEqual(s,t)==False

s = "4432.19(9)"
t = "4432.2(0)"
assert Solution().isRationalEqual(s,t)

s = "2.(2)"
t = "2"
assert Solution().isRationalEqual(s,t)==False



s = "0.(52)"
t = "0.5(25)"
assert Solution().isRationalEqual(s,t)

s = "0.1666(6)"
t = "0.166(66)"
assert Solution().isRationalEqual(s,t)