#
# @lc app=leetcode.cn id=1187 lang=python3
#
# [1187] 使数组严格递增
#
from sbw import *
# @lc code=start

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        inf=float('inf')
        arr1=[-1]+arr1+[inf]
        L1=len(arr1)
        arr2=sorted(set(arr2))
        L2=len(arr2)
        f=[inf]*(L1)
        f[0]=0
        for i in range(1,L1):
            if arr1[i]>arr1[i-1]:
                f[i]=min(f[i],f[i-1])
            
            k=bisect_left(arr2,arr1[i])
            for j in range(1,min(k,i-1)+1):
                if arr2[k-j]>arr1[i-j-1]:
                    f[i]=min(f[i],f[i-j-1]+j)
        return f[-1] if f[-1]<inf else -1

# @lc code=end
assert Solution().makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [4,3,1])==2
assert Solution().makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [1,3,2,4])==1
