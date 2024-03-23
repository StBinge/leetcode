#
# @lc app=leetcode.cn id=1420 lang=python3
#
# [1420] 生成数组
#

# @lc code=start
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if n<k or m<k:
            return 0
        Mod=10**9+7
        # f=[[[0]*(m+1) for _ in range(k+1)] for _ in range(n)]
        f0=[[0]*(m+1) for _ in range(k+1)]
        f1=[[0]*(m+1) for _ in range(k+1)]
        for i in range(1,m+1):
            f0[1][i]=1
        for i in range(1,n):
            for s in range(1,min(i+1,k)+1):
                presum_j=0
                for j in range(1,m+1):
                    f1[s][j]=(f0[s][j]*j + presum_j)%Mod
                    presum_j+=f0[s-1][j]
                    # f[i][s][j]=(f[i-1][s][j]*j+presum_j)%Mod
                    # presum_j=(presum_j+f[i-1][s-1][j])%Mod
            f0,f1=f1,f0

        return sum(f0[-1])%Mod
# @lc code=end
assert Solution().numOfArrays(50,100,25)==34549172
assert Solution().numOfArrays(n = 5, m = 2, k = 3)==0
assert Solution().numOfArrays(2,3,1)==6
