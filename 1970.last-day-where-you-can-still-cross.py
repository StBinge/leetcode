#
# @lc app=leetcode.cn id=1970 lang=python3
# @lcpr version=30204
#
# [1970] 你能穿过矩阵的最后一天
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # left_col=0
        # right_col=col+1
        p = {}
        sz = {}

        def find(x):
            px = p.setdefault(x, x)
            if x != px:
                p[x] = find(px)
            return p[x]

        def connect(x, y):
            x, y = find(x), find(y)
            sx = sz.get(x, 1)
            sy = sz.get(y, 1)
            if sx > sy:
                x, y = y, x
            p[x] = y
            sz[y] = sx + sy

        top = (0, 0)
        bottom = (row + 1, row + 1)
        waters = set()
        for i in range(len(cells) - 1, -1, -1):
            dirs = [-1, 0, 1, 0, -1]
            r, c = cells[i]
            for j in range(4):
                nr, nc = r + dirs[j], c + dirs[j + 1]
                if nr == 0:
                    connect(top, (r, c))
                elif nr == row + 1:
                    connect(bottom, (r, c))
                if (nr, nc) in waters:
                    connect((r, c), (nr, nc))
            if find(top) == find(bottom):
                return i
            waters.add((r, c))


# @lc code=end
assert (
    Solution().latestDayToCross(
        row=3,
        col=3,
        cells=[[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]],
    )
    == 3
)
assert (
    Solution().latestDayToCross(row=2, col=2, cells=[[1, 1], [1, 2], [2, 1], [2, 2]])
    == 1
)
assert (
    Solution().latestDayToCross(row=2, col=2, cells=[[1, 1], [2, 1], [1, 2], [2, 2]])
    == 2
)


#
# @lcpr case=start
# 2\n2\n[[1,1],[2,1],[1,2],[2,2]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n2\n[[1,1],[1,2],[2,1],[2,2]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n3\n[[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]\n
# @lcpr case=end

#
