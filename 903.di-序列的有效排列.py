#
# @lc app=leetcode.cn id=903 lang=python3
#
# [903] DI 序列的有效排列
#

# @lc code=start
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        sz=len(s)
        f=[[0]*(sz+1) for _ in range(sz+1)]
        f[0][0]=1
        Mod=10**9+7
        for i in range(1,sz+1):
            if s[i-1]=='D':
                f[i][i]=0
                for j in range(i-1,-1,-1):
                    f[i][j]=(f[i][j+1]+f[i-1][j])%Mod
            else:
                f[i][0]=0
                for j in range(1,i+1):
                    f[i][j]=(f[i][j-1]+f[i-1][j-1])%Mod
        return sum(f[-1])%Mod
# @lc code=end
assert Solution().numPermsDISequence('DID')==5
