#
# @lc app=leetcode.cn id=1502 lang=python3
#
# [1502] 判断能否形成等差数列
#
from sbw import *
# @lc code=start
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d=arr[0]-arr[1]
        for i in range(1,len(arr)-1):
            if arr[i]-arr[i+1]!=d:
                return False
        return True
# @lc code=end

