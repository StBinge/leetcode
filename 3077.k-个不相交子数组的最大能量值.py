#
# @lc app=leetcode.cn id=3077 lang=python3
#
# [3077] K 个不相交子数组的最大能量值
#
from sbw import *
# @lc code=start
class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        L=len(nums)
        presums=list(accumulate(nums,initial=0))

        f=[0]*(L+1)

        for i in range(1,k+1):
            pre=f[i-1]
            f[i-1]=mx=float('-inf')
            w=(-1)**(i+1)*(k-i+1)
            for j in range(i,L-k+i+1):
                mx=max(mx,pre-presums[j-1]*w)
                pre=f[j]
                f[j]=max(f[j-1],presums[j]*w+mx)
        return f[-1]
# @lc code=end

assert Solution().maximumStrength(nums = [1,2,3,-1,2], k = 3)==22