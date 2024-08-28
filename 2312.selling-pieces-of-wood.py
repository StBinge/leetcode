#
# @lc app=leetcode.cn id=2312 lang=python3
# @lcpr version=30204
#
# [2312] 卖木头块
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        # f[height][width]
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i, j, p in prices:
            f[i][j] = p
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                f[i][j] = max(
                    f[i][j],
                    max(
                        (f[i][k] + f[i][j - k] for k in range(1, j // 2 + 1)), default=0
                    ),
                    max(
                        (f[k][j] + f[i - k][j] for k in range(1, i // 2 + 1)), default=0
                    ),
                )
        return f[m][n]


# @lc code=end
assert Solution().sellingWood(m=3, n=5, prices=[[1, 4, 2], [2, 2, 7], [2, 1, 3]]) == 19
assert Solution().sellingWood(m=4, n=6, prices=[[3, 2, 10], [1, 4, 2], [4, 1, 3]]) == 32


#
# @lcpr case=start
# 3\n5\n[[1,4,2],[2,2,7],[2,1,3]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n6\n[[3,2,10],[1,4,2],[4,1,3]]\n
# @lcpr case=end

#
