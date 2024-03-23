#
# @lc app=leetcode.cn id=3017 lang=python3
#
# [3017] 按距离统计房屋对数目 II
#
from sbw import *
# @lc code=start
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x>y:
            x,y=y,x
        if y-x<=1:
            return list(v*2 for v in range(n-1,-1,-2))
        
        dif=[0]*(n+1)
        def add(l,r):
            dif[l]+=2
            dif[r+1]-=2
# @lc code=end

