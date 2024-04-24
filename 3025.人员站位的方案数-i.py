#
# @lc app=leetcode.cn id=3025 lang=python3
#
# [3025] 人员站位的方案数 I
#
from sbw import *


# @lc code=start
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: [x[0], -x[1]])
        ret = 0
        L = len(points)
        for i in range(L):
            y1 = points[i][1]
            ma = float("-inf")
            for j in range(i + 1, L):
                y2 = points[j][1]
                if ma < y2 <= y1:
                    ret += 1
                    ma = y2
        return ret


# @lc code=end

assert Solution().numberOfPairs([[3, 1], [1, 3], [1, 1]]) == 2
assert Solution().numberOfPairs([[6, 2], [4, 4], [2, 6]]) == 2
assert Solution().numberOfPairs([[1, 1], [2, 2], [3, 3]]) == 0
