#
# @lc app=leetcode.cn id=1499 lang=python3
#
# [1499] 满足不等式的最大值
#
from sbw import *
# @lc code=start

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        L=len(points)
        ret=float('-inf')
        q=deque()
        for x,y in points:
            while q and q[0][1]+k<x:
                q.popleft()
            if q:
                ret=max(ret,x+y+q[0][0])
            z=y-x
            while q and q[-1][0]<z:
                q.pop()
            q.append([z,x])
        return ret
# @lc code=end+y
assert Solution().findMaxValueOfEquation([[-19,9],[-15,-19],[-5,-8]],10)==-6
assert Solution().findMaxValueOfEquation(points = [[0,0],[3,0],[9,2]], k = 3)==3
assert Solution().findMaxValueOfEquation(points = [[1,3],[2,0],[5,10],[6,-10]], k = 1)==4
