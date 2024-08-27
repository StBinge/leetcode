#
# @lc app=leetcode.cn id=1655 lang=python3
#
# [1655] 分配重复整数
#
from sbw import *


# @lc code=start
class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        counter = list(Counter(nums).values())
        N=len(counter)
        M=len(quantity)
        # f=[[False]*(N+1) for _ in range(1<<M)]
        # f[0][0]=True
        needs=[0]*(1<<M)
        for i in range(1,1<<M):
            for j in range(M):
                if i & (1<<j):
                    needs[i]=needs[i-(1<<j)]+quantity[j]
                    break
        f0=[False]*(1<<M)
        f0[0]=True
        f1=f0.copy()
        for i in range(N):
            for mask in range(1,1<<M):
                 if f0[mask]:
                     f1[mask]=True
                     continue
                 sub_mask=mask
                 while sub_mask:
                    pre_mask=mask ^ sub_mask
                    if f0[pre_mask] and needs[sub_mask]<=counter[i]:
                        f1[mask]=True
                        break
                    sub_mask=(sub_mask-1) & mask
            if f1[-1]:
                return True
            f0,f1=f1,f0
        return False


# @lc code=end
assert Solution().canDistribute([74,580,649,649,870,791,19,649,74,216,501,115,403,74,732,48,649,131,311,869,944,216,649,326,319,609,43,649],[5,3])
assert Solution().canDistribute(nums = [1,1,2,2], quantity = [2,2])
assert Solution().canDistribute([1,1,2,3],[2,2])==False
assert Solution().canDistribute([108,774,486,774,297,486,980,774,108,774,774,980,108,486,108,486,108,486,297,297,774,486,774,980,980,980,108,297,774,980,297,774,108,980,486,108,297,486,486,297,297,774,774,486,297],[3,3,3,7,8,5,5,11])
assert Solution().canDistribute([1,1,1,1,1],[2,3])
assert Solution().canDistribute(nums = [1,2,3,3], quantity = [2])
assert Solution().canDistribute(nums=[1, 2, 3, 4], quantity=[2]) == False
