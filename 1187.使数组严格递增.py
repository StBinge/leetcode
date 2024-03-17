#
# @lc app=leetcode.cn id=1187 lang=python3
#
# [1187] 使数组严格递增
#
from sbw import *
# @lc code=start
import bisect
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        inf=float('inf')
        arr1=[-1]+arr1+[inf]
        L1=len(arr1)
        arr2=sorted(set(arr2))
        L2=len(arr2)
        inf=float('inf')
        f=[inf]*(L1+2)
        f[0]=0
        arr1=[-1]+arr1+[inf]
        for i in range(1,L1+2):
            if arr1[i]>arr1[i-1]:
                f[i]=min(f[i],f[i-1])
            k=bisect.bisect_left(arr2,arr1[i])-1
            if k>=0:
                for j in range(1,min(i-1,k+1)+1):
                    if arr1[i-j-1]<arr2[k-j+1]:
                        f[i]=min(f[i],f[i-j-1]+j)

        return f[-1] if f[-1]<inf else -1


# @lc code=end
assert Solution().makeArrayIncreasing([5,16,19,2,1,12,7,14,5,16],
[6,17,4,3,6,13,4,3,18,17,16,7,14,1,16])==8
assert Solution().makeArrayIncreasing([1,5,3,6,7],
[1,6,3,3])==-1
assert Solution().makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [4,3,1])==2
assert Solution().makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [1,3,2,4])==1
