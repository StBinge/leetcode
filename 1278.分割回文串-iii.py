#
# @lc app=leetcode.cn id=1278 lang=python3
#
# [1278] 分割回文串 III
#
from sbw import *
# @lc code=start
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        L=len(s)
        cost=[[0]*L for _ in range(L)]
        for span in range(2,L+1):
            for i in range(L-span+1):
                j=i+span-1
                cost[i][j]=cost[i+1][j-1]+int(s[i]!=s[j])
        f=[[100]*(k+1) for _ in range(L+1)]
        
        f[0][0]=0
        # f[1][1]=0
        for i in range(1,L+1):
            f[i][1]=cost[0][i-1]
            for j in range(1,min(k,i)+1):
                f[i]
                for ii in range(j-1,i):
                    f[i][j]=min(f[i][j],f[ii][j-1]+cost[ii][i-1])
                    if f[i][j]==0:
                        break
        return f[-1][k]
# @lc code=end

assert Solution().palindromePartition(s = "tcymekt", k = 4)==2
assert Solution().palindromePartition(s = "leetcode", k = 8)==0
assert Solution().palindromePartition(s = "aabbc", k = 3)==0
assert Solution().palindromePartition('abc',2)==1