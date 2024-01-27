#
# @lc app=leetcode.cn id=1237 lang=python3
#
# [1237] 找出给定方程的正整数解
#
from sbw import *
class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        return x+y
  
# @lc code=start
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
import bisect
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ret=[]
        y=1000
        for x in range(1,1001):
            while y and customfunction.f(x,y)>z:
                y-=1
            if y==0:
                break
            if customfunction.f(x,y)==z:
                ret.append([x,y])
                y-=1
        return ret

# @lc code=end
assert sorted(Solution().findSolution(CustomFunction(),5))==[[1,4],[2,3],[3,2],[4,1]]
