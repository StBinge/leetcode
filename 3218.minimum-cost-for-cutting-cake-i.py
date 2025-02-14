#
# @lc app=leetcode.cn id=3218 lang=python3
# @lcpr version=30204
#
# [3218] 切蛋糕的最小总开销 I
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumCost(
        self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]
    ) -> int:
        horizontalCut.sort()# m-1
        verticalCut.sort()# n-1
        v = h = 0
        ret = 0
        for _ in range(m + n - 2):
            if v == n-1 or h < m-1 and horizontalCut[h] < verticalCut[v]:
                ret += horizontalCut[h] * (n-v)
                h += 1
            else:
                ret += verticalCut[v] * (m-h)
                v += 1
        return ret


# @lc code=end
assert Solution().minimumCost(m=2, n=2, horizontalCut=[7], verticalCut=[4]) == 15
assert Solution().minimumCost(m=3, n=2, horizontalCut=[1, 3], verticalCut=[5]) == 13


#
# @lcpr case=start
# 3\n2\n[1,3]\n[5]\n
# @lcpr case=end

# @lcpr case=start
# 2\n2\n[7]\n[4]\n
# @lcpr case=end

#
