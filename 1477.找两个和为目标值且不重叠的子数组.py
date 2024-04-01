#
# @lc app=leetcode.cn id=1477 lang=python3
#
# [1477] 找两个和为目标值且不重叠的子数组
#
from sbw import *
# @lc code=start
# import heapq
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        l=0
        L=len(arr)
        s=0
        f=[0]*(L+1)
        f[0]=float('inf')
        ret=L+1
        for i in range(L):
            s+=arr[i]
            while s>target:
                s-=arr[l]
                l+=1
            if s==target:
                length=i-l+1
                f[i+1]=min(length,f[i])
                ret=min(ret,f[l]+length)
            else:
                f[i+1]=f[i]
        return ret if ret<=L else -1

# @lc code=end
assert Solution().minSumOfLengths(arr = [3,1,1,1,5,1,2,1], target = 3)==3
assert Solution().minSumOfLengths(arr = [5,5,4,4,5], target = 3)==-1
assert Solution().minSumOfLengths(arr = [4,3,2,6,2,3,4], target = 6)==-1
assert Solution().minSumOfLengths(arr = [7,3,4,7], target = 7)==2
assert Solution().minSumOfLengths(arr = [3,2,2,4,3], target = 3)==2
