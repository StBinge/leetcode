#
# @lc app=leetcode.cn id=1870 lang=python3
#
# [1870] 准时到达的列车最小时速
#
from sbw import *


# @lc code=start
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1
        hour=round(hour*100)
        left = 1
        right = max(dist) * 101
        while left < right:
            speed = (left + right) >> 1
            time = 0
            for d in dist[:-1]:
                time += (d-1)//speed+1
            tot=time*speed
            tot+=dist[-1]
            if tot*100 <= hour*speed:
                right = speed
            else:
                left = speed + 1
        return left


# @lc code=end
assert Solution().minSpeedOnTime([1, 1, 100000], 2.01) == 10000000
assert Solution().minSpeedOnTime(dist=[1, 3, 2], hour=1.9) == -1
assert Solution().minSpeedOnTime(dist=[1, 3, 2], hour=2.7) == 3
assert Solution().minSpeedOnTime(dist=[1, 3, 2], hour=6) == 1
