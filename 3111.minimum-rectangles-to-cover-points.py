#
# @lc app=leetcode.cn id=3111 lang=python3
# @lcpr version=30204
#
# [3111] 覆盖所有点的最少矩形数目
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort()
        ret = 1
        right = points[0][0] + w
        for x, y in points:
            if x > right:
                right = x + w
                ret += 1
        return ret


# @lc code=end
assert (
    Solution().minRectanglesToCoverPoints(
        points=[[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]], w=2
    )
    == 3
)
assert (
    Solution().minRectanglesToCoverPoints(
        points=[[2, 1], [1, 0], [1, 4], [1, 8], [3, 5], [4, 6]], w=1
    )
    == 2
)


#
# @lcpr case=start
# [[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[2,3],[1,2]]\n0\n
# @lcpr case=end

#
