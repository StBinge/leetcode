#
# @lc app=leetcode.cn id=3122 lang=python3
# @lcpr version=30204
#
# [3122] 使矩阵满足条件的最少操作次数
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        f0, f1, pre = 0, 0, -1
        for col in zip(*grid):
            mx, mx1, x = f0, 0, -1
            for k, v in Counter(col).items():
                cur = v + (f0 if k != pre else f1)
                if cur > mx:
                    mx, mx1, pre = cur, mx, k
                elif cur > mx1:
                    mx1 = cur
            f0, f1, pre = mx, mx1, x
        return R * C - f0


# @lc code=end
assert Solution().minimumOperations([[1, 1, 1], [0, 0, 0]]) == 3
assert Solution().minimumOperations([[1, 1, 1], [0, 0, 0]]) == 3
assert Solution().minimumOperations([[1, 0, 2], [1, 0, 2]]) == 0


#
# @lcpr case=start
# [[1,0,2],[1,0,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,1],[0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1],[2],[3]]\n
# @lcpr case=end

#
