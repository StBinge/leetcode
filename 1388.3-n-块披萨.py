#
# @lc app=leetcode.cn id=1388 lang=python3
#
# [1388] 3n 块披萨
#
from sbw import *
# @lc code=start
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        def dp(ar:list):
            L=len(ar)
            n=L//3+1
            # f=[[float('-inf')]*(n+1) for _ in range(L)]
            f1=[float('-inf')]*(n+1)
            f2=[float('-inf')]*(n+1)
            
            # f[0][0]=0
            # f[0][1]=ar[0]
            # f[1][0]=0
            # f[1][1]=max(ar[:2])
            f1[0]=f2[0]=0
            f1[1]=ar[0]
            f2[1]=max(ar[:2])

            for i in range(2,L):
                f=[float('-inf')]*(n+1)
                f[0]=0
                for j in range(1,n+1):
                    f[j]=max(ar[i]+f1[j-1],f2[j])
                f1,f2=f2,f
            return f2[-1]
        
        r1=dp(slices[1:])
        r2=dp(slices[:-1])
        return max(r1,r2)

# @lc code=end
assert Solution().maxSizeSlices([8,9,8,6,1,1])==16
assert Solution().maxSizeSlices([1,2,3,4,5,6])==10
