#
# @lc app=leetcode.cn id=1187 lang=python3
#
# [1187] 使数组严格递增
#
from sbw import *
# @lc code=start

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        L1=len(arr1)
        arr2=sorted(set(arr2))
        L2=len(arr2)
        inf=float('-inf')
        f=[[inf]*(L2+1) for _ in range(L1+1)]
        f[0][0]=-1
        idx2=0
        for i in range(1,L1+1):
            for j in range(1,min(i,L2)+1):
                if arr1[i]>f[i-1][j]:
                    f[i][j]=arr1[i]
                

# @lc code=end
assert Solution().makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [4,3,1])==2
assert Solution().makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [1,3,2,4])==1
