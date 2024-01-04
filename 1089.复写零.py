#
# @lc app=leetcode.cn id=1089 lang=python3
#
# [1089] 复写零
#
from sbw import *
# @lc code=start
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        L=len(arr)
        offset=sum(1 for n in arr if n==0)
        for i in range(L-1,-1,-1):
            if arr[i]==0:
                offset-=1
                continue
            _n=arr[i]
            arr[i]=0
            if i+offset<L:
                arr[i+offset]=_n


# @lc code=end
arr = [1,2,3]
Solution().duplicateZeros(arr)
assert arr==[1,2,3]

arr = [1,0,2,3,0,4,5,0]
Solution().duplicateZeros(arr)
assert arr==[1,0,0,2,3,0,0,4]
