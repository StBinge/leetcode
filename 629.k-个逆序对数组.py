#
# @lc app=leetcode.cn id=629 lang=python3
#
# [629] K 个逆序对数组
#

# @lc code=start
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        f=[0]*(k+1)
        f[0]=1
        for i in range(1,n+1):
            g=[0]*(k+1)

            for j in range(k+1):
                g[j]=(g[j-1] if j>0 else 0) - (f[j-i] if j>=i else 0) +f[j]
                g[j]=g[j]%(10**9+7)
            f=g
        return f[-1]
# @lc code=end

assert Solution().kInversePairs(3,1)==2
assert Solution().kInversePairs(3,0)==1