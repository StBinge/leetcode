#
# @lc app=leetcode.cn id=1238 lang=python3
#
# [1238] 循环码排列
#
from sbw import *
# @lc code=start
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        ret=[0]*(1<<n)
        for i in range(1<<n):
            ret[i]=i>>1 ^ i ^ start
        return ret
# @lc code=end

