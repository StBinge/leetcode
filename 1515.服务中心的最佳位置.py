#
# @lc app=leetcode.cn id=1515 lang=python3
#
# [1515] 服务中心的最佳位置
#
from sbw import *

# @lc code=start
import math, random


class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        if len(positions) == 1:
            return 0
        eps = 1e-7

        def total_dist(x, y):
            return sum(math.sqrt((x - px) ** 2 + (y - py) ** 2) for px, py in positions)

        def gradient(cx, cy):
            dx, dy = 0, 0
            for x, y in positions:
                dx += (cx - x) / (math.sqrt((cx - x) ** 2 + (cy - y) ** 2) + eps)
                dy += (cy - y) / (math.sqrt((cx - x) ** 2 + (cy - y) ** 2) + eps)
            return dx, dy

        step = 1
        x = sum(p[0] for p in positions) / len(positions)
        y = sum(p[1] for p in positions) / len(positions)
        while True:
            random.shuffle(positions)
            px, py = x, y
            dx, dy = gradient(x, y)
            x -= dx * step
            y -= dy * step
            step *= (1 - 0.001)
            if math.sqrt((px - x) ** 2 + (py - y) ** 2) < eps:
                return total_dist(x, y)


# @lc code=end
def test(positions, result):
    eps = 1e-5
    ans = Solution().getMinDistSum(positions)
    assert abs(ans - result) <= eps, f"{result}\t{ans}"


test(
    [
        [4, 4],
        [52, 89],
        [76, 60],
        [4, 4],
        [4, 4],
        [93, 59],
        [50, 92],
        [4, 4],
        [76, 14],
        [4, 4],
        [46, 41],
        [4, 4],
        [4, 4],
        [4, 4],
        [4, 4],
        [67, 14],
        [73, 71],
        [83, 44],
        [4, 4],
        [4, 4],
        [4, 4],
        [4, 4],
        [30, 29],
        [74, 77],
        [4, 4],
        [4, 4],
        [4, 4],
        [26, 62],
        [4, 4],
        [4, 4],
        [50, 30],
        [44, 93],
    ],
    1119.58582,
)
test([[1, 1], [0, 0], [2, 0]], 2.73205)
test([[1, 1]], 0)
test([[1, 1], [3, 3]], 2.82843)
test([[0, 1], [1, 0], [1, 2], [2, 1]], 4)
