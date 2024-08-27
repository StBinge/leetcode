#
# @lc app=leetcode.cn id=1625 lang=python3
#
# [1625] 执行操作后字典序最小的字符串
#
from sbw import *
# @lc code=start
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        N=len(s)
        ret=[int(c) for c in s]
        s=ret+ret
        g=math.gcd(N,b)

        def set_small(t:list,idx):
            mi=t[idx]
            time=0
            for i in range(1,10):
                t[idx]=(t[idx]+a)%10
                if t[idx]<mi:
                    mi=t[idx]
                    time=i
            t[idx]=mi
            for i in range(idx+2,N,2):
                t[i]=(t[i]+time*a)%10
            return t

        for i in range(0,N,g):
            t=s[i:i+N]
            set_small(t,1)
            if b&1:
                set_small(t,0)
            if t<ret:
                ret=t
        return ''.join(map(str,ret))
# @lc code=end

assert Solution().findLexSmallestString('5525',9,2)=='2050'