#
# @lc app=leetcode.cn id=942 lang=python3
#
# [942] 增减字符串匹配
#
from sympy import numer
from sbw import *
# @lc code=start
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        N=len(s)
        lo,hi=0,N
        ret=[]
        for c in s:
            if c=='I':
                ret.append(lo)
                lo+=1
            else:
                ret.append(hi)
                hi-=1
        ret.append(lo)
        return ret
# @lc code=end
def check(s,ret):
    for i,c in enumerate(s):
        if c=='I' and ret[i]>ret[i+1]:
            return False
        if c=='D' and ret[i]<ret[i+1]:
            return False
    return True
s = "D"
ret=Solution().diStringMatch(s)
assert check(s,ret)

s = "IDID"
ret=Solution().diStringMatch(s)
assert check(s,ret)

s = "III"
ret=Solution().diStringMatch(s)
assert check(s,ret)

s = "DDI"
ret=Solution().diStringMatch(s)
assert check(s,ret)