#
# @lc app=leetcode.cn id=1631 lang=python3
#
# [1631] 最小体力消耗路径
#
from sbw import *


# @lc code=start
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R, C = len(heights), len(heights[0])
        if R * C == 1:
            return 0
        p = list(range(R * C))
        size = [1] * (R * C)

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if size[px] < size[py]:
                px, py = py, px
            p[py] = px
            size[px] += size[py]

        edges = []
        for r in range(R):
            for c in range(C):
                if r > 0:
                    edges.append(
                        [
                            abs(heights[r][c] - heights[r - 1][c]),
                            r * C + c,
                            (r - 1) * C + c,
                        ]
                    )
                if c > 0:
                    edges.append(
                        [
                            abs(heights[r][c] - heights[r][c - 1]),
                            r * C + c,
                            r * C + c - 1,
                        ]
                    )
        edges.sort()
        for w, x, y in edges:
            union(x, y)
            if find(0) == find(R * C - 1):
                return w


# @lc code=end
assert (
    Solution().minimumEffortPath(
        [
            [1, 2, 1, 1, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 1, 1, 2, 1],
        ]
    )
    == 0
)
assert Solution().minimumEffortPath([[3]]) == 0
assert Solution().minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1
assert Solution().minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2
