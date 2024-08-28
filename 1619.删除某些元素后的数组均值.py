#
# @lc app=leetcode.cn id=1619 lang=python3
#
# [1619] 删除某些元素后的数组均值
#
from sbw import *
# @lc code=start
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        N=len(arr)
        k=N*5//100
        return sum(arr[k:N-k])/(N-2*k)
# @lc code=end

