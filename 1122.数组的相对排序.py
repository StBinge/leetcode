#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#
from sbw import *
# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        L=len(arr2)
        s={n:i for i,n in enumerate(arr2)}
        arr1.sort(key=lambda n:s.get(n,n+L))
        return arr1
        
# @lc code=end
assert Solution().relativeSortArray(arr1 = [26,21,11,20,50,34,1,18], arr2 = [21,11,26,20])==[21,11,26,20,1,18,34,50]
assert Solution().relativeSortArray(arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6])==[22,28,8,6,17,44]
assert Solution().relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6])==[2,2,2,1,4,3,3,9,6,7,19]
