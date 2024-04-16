#
# @lc app=leetcode.cn id=3082 lang=python3
#
# [3082] 求出所有子序列的能量和
#
from sbw import *
# @lc code=start
class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        Mod=10**9+7
        L=len(nums)
        # f=[[0]*(k+1) for _ in range(L+1)]
        f=[0]*(k+1)
        f[0]=1
        for i in range(L):
            for j in range(k,-1,-1):
                f[j]=f[j]*2
                if j>=nums[i]:
                    f[j]+=f[j-nums[i]]
                f[j]%=Mod
        return f[-1]
        
# @lc code=end
assert Solution().sumOfPower(nums = [1,2,3], k = 3)==6
