#
# @lc app=leetcode.cn id=1175 lang=python3
#
# [1175] 质数排列
#

# @lc code=start
from math import perm
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        flag=[True]*(n+1)
        flag[1]=False
        for i in range(2,n//2+1):
            for j in range(2,n):
                if i*j>n:
                    break
                flag[i*j]=False
        cnt=sum(mark for mark in flag[1:])
        return perm(cnt,cnt)*perm(n-cnt,n-cnt)%(10**9+7)
# @lc code=end

assert Solution().numPrimeArrangements(100)==682289015
assert Solution().numPrimeArrangements(5)==12