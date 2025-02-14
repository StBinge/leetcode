#
# @lc app=leetcode.cn id=2245 lang=python3
# @lcpr version=30204
#
# [2245] 转角路径的乘积中最多能有几个尾随零
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        fac2 = [0] * 1001
        fac5 = [0] * 1001
        for i in range(1, 1001):
            if i % 2 == 0:
                fac2[i] = fac2[i // 2] + 1
            if i % 5 == 0:
                fac5[i] = fac5[i // 5] + 1

        R, C = len(grid), len(grid[0])
        cols_sum = [[[0, 0]] for _ in range(C)]
        rows_sum = [[[0, 0]] for _ in range(R)]
        for r in range(R):
            for c in range(C):
                f2 = fac2[grid[r][c]]
                f5 = fac5[grid[r][c]]
                p2, p5 = cols_sum[c][-1]
                cols_sum[c].append([p2 + f2, p5 + f5])
                p2, p5 = rows_sum[r][-1]
                rows_sum[r].append([p2 + f2, p5 + f5])

        ret = 0
        for r in range(R):
            for c in range(C):
                row_sum = rows_sum[r]
                col_sum = cols_sum[c]
                cur2, cur5 = fac2[grid[r][c]], fac5[grid[r][c]]
                row2, row5 = row_sum[-1]
                col2, col5 = col_sum[-1]
                top = col_sum[r + 1]
                left = row_sum[c + 1]
                bottom = col2 - col_sum[r][0], col5 - col_sum[r][1]
                right = row2 - row_sum[c][0], row5 - row_sum[c][1]
                for i2, i5 in [top, bottom]:
                    for j2, j5 in [left, right]:
                        ret = max(ret, min(i2 + j2 - cur2, i5 + j5 - cur5))
        return ret


# @lc code=end
assert (
    Solution().maxTrailingZeros(
        [
            [899, 727, 165, 249, 531, 300, 542, 890],
            [981, 587, 565, 943, 875, 498, 582, 672],
            [106, 902, 524, 725, 699, 778, 365, 220],
        ]
    )
    == 5
)
assert Solution().maxTrailingZeros([[4, 3, 2], [7, 6, 1], [8, 8, 8]]) == 0
assert Solution().maxTrailingZeros([[4, 3, 2], [7, 6, 1], [8, 8, 8]]) == 0
assert (
    Solution().maxTrailingZeros(
        grid=[
            [23, 17, 15, 3, 20],
            [8, 1, 20, 27, 11],
            [9, 4, 6, 2, 21],
            [40, 9, 1, 10, 6],
            [22, 7, 4, 5, 3],
        ]
    )
    == 3
)


#
# @lcpr case=start
# [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,3,2],[7,6,1],[8,8,8]]\n
# @lcpr case=end

#
