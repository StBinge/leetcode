#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#
from typing import List
# @lc code=start
from functools import cache
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        L=len(strs)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(L):
            zero=one=0
            for c in strs[i]:
                if c=='0':
                    zero+=1
                else:
                    one+=1
            for z in range(m,zero-1,-1):
                for o in range(n,one-1,-1):
                    dp[z][o]=max(dp[z][o],dp[z-zero][o-one]+1)
        return dp[-1][-1]
# @lc code=end
strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
assert Solution().findMaxForm(strs,m,n)==4

strs = ["10", "0", "1"]
m = 1
n = 1
assert Solution().findMaxForm(strs,m,n)==2
