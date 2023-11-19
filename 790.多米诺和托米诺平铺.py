#
# @lc app=leetcode.cn id=790 lang=python3
#
# [790] 多米诺和托米诺平铺
#

# @lc code=start
class Solution:
    def numTilings(self, n: int) -> int:
        f=[[0]*4 for _ in range(n+1)]
        f[0][3]=1
        Mod=10**9+7
        for i in range(1,n+1):
            f[i][0]=f[i-1][3]
            f[i][1]=f[i-1][0]+f[i-1][2]
            f[i][2]=f[i-1][0]+f[i-1][1]
            f[i][3]=f[i-1][0]+f[i-1][1]+f[i-1][2]+f[i-1][3]
        return f[n][3]%Mod
# @lc code=end

assert Solution().numTilings(3)==5
assert Solution().numTilings(4)==11
assert Solution().numTilings(1)==1