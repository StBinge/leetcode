#
# @lc app=leetcode.cn id=1012 lang=python3
#
# [1012] 至少有 1 位重复的数字
#
from sbw import *
# @lc code=start
from math import perm
class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        limit=list(map(int,str(N+1)))
        L=len(limit)
        ret=sum(9*perm(9,i) for i in range(L-1))
        mask=0
        for i,d in enumerate(limit):
            for x in range(i==0,d):
                x+=1
                if mask & (1<<x):
                    continue
                ret+=perm(9-i,L-1-i)
            if mask & (1<<(d+1)):
                break
            mask^=(1<<(d+1))
        return N-ret

# @lc code=end
assert Solution().numDupDigitsAtMostN(20)==1
assert Solution().numDupDigitsAtMostN(8646800)==8010590
assert Solution().numDupDigitsAtMostN(100)==10
assert Solution().numDupDigitsAtMostN(1000)==262
