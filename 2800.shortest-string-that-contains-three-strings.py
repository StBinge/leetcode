#
# @lc app=leetcode.cn id=2800 lang=python3
# @lcpr version=30204
#
# [2800] 包含三个字符串的最短字符串
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
import itertools
class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def concat(x:str,y:str):
            if x.find(y)>=0:
                return x
            if y.find(x)>=0:
                return y
            lx,ly=len(x),len(y)
            for cnt in range(min(lx,ly),0,-1):
                if x[-cnt:]==y[:cnt]:
                    return x+y[cnt:]
            return x+y
        
        ret='z'*300
        for x,y,z in itertools.permutations([a,b,c],3):
            s=concat(concat(x,y),z)
            if len(s)<len(ret):
                ret=s
            elif len(s)==len(ret):
                ret=min(ret,s)
        return ret
        
# @lc code=end
assert Solution().minimumString('ca','a','a')=='ca'
assert Solution().minimumString(a = "ab", b = "ba", c = "aba")=='aba'
assert Solution().minimumString(a = "abc", b = "bca", c = "aaa")=='aaabca'


#
# @lcpr case=start
# "abc"\n"bca"\n"aaa"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"ba"\n"aba"\n
# @lcpr case=end

#

