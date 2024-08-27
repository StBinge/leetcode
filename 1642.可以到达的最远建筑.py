#
# @lc app=leetcode.cn id=1642 lang=python3
#
# [1642] 可以到达的最远建筑
#
from sbw import *


# @lc code=start
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        N = len(heights)
        if ladders == 0:
            pre = 10**6
            for i, h in enumerate(heights):
                if pre >= h:
                    pre = h
                    continue
                bricks -= h - pre
                pre = h
                if bricks < 0:
                    return i - 1
            return N - 1

        used_ladders = []
        pre = 10**6

        for i, h in enumerate(heights):
            if pre >= h:
                pre = h
                continue
            dif = h - pre
            pre = h
            if len(used_ladders) < ladders:
                heapq.heappush(used_ladders, dif)
                continue
            if dif <= used_ladders[0]:
                bricks -= dif
                if bricks < 0:
                    return i - 1
                continue

            b = heapq.heappushpop(used_ladders, dif)
            bricks -= b
            if bricks < 0:
                return i - 1
        return N - 1


# @lc code=end
assert Solution().furthestBuilding([4, 2, 6, 6, 9, 8, 9, 12], 5, 0) == 3
assert (
    Solution().furthestBuilding(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1)
    == 4
)
assert Solution().furthestBuilding(heights=[14, 3, 19, 3], bricks=17, ladders=0) == 3
assert (
    Solution().furthestBuilding(
        heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2
    )
    == 7
)
