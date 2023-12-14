#
# @lc app=leetcode.cn id=978 lang=python3
#
# [978] 最长湍流子数组
#
from sbw import *


# @lc code=start
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L = len(arr)
        if L==1:
            return 1
        f0,f1=1,1
        ret=1
        for i in range(1,L):
            if arr[i-1]>arr[i]:
                f0,f1=f1+1,1
            elif arr[i-1]<arr[i]:
                f0,f1=1,f0+1
            else:
                f0=f1=1
            ret=max(ret,f0,f1)

        return ret


# @lc code=end
arr=[37,199,60,296,257,248,115,31,273,176]
assert Solution().maxTurbulenceSize(arr) == 5

arr = [4, 8, 12, 16]
assert Solution().maxTurbulenceSize(arr) == 2

arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
assert Solution().maxTurbulenceSize(arr) == 5
