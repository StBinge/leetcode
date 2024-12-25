#
# @lc app=leetcode.cn id=2596 lang=python3
# @lcpr version=30204
#
# [2596] 检查骑士巡视方案
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0:
            return False
        R, C = len(grid), len(grid[0])
        pos = {}
        for row in grid:
            row = [str(cell).rjust(2) for cell in row]
            print(row)
        for r in range(R):
            for c in range(C):
                pos[grid[r][c]] = [r, c]

        for i in range(R * C - 1):
            r1, c1 = pos[i]
            r2, c2 = pos[i + 1]
            if abs(r1 - r2) * abs(c1 - c2) != 2:
                return False
        return True


# @lc code=end
assert (
    Solution().checkValidGrid(
        [
            [24, 11, 22, 17, 4],
            [21, 16, 5, 12, 9],
            [6, 23, 10, 3, 18],
            [15, 20, 1, 8, 13],
            [0, 7, 14, 19, 2],
        ]
    )
    == False
)


#
# @lcpr case=start
# [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,3,6],[5,8,1],[2,7,4]]\n
# @lcpr case=end

#
