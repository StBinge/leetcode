#
# @lc app=leetcode.cn id=3143 lang=python3
# @lcpr version=30204
#
# [3143] 正方形中的最多点数
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        min_edge=defaultdict(lambda :float('inf'))
        mi_edge=float('inf')
        for [x,y],c in zip(points,s):
            e=max(abs(x),abs(y))
            if e<min_edge[c]:
                mi_edge=min(mi_edge,min_edge[c])
                min_edge[c]=e
            else:
                mi_edge=min(mi_edge,e)
        return sum(v<mi_edge for v in min_edge.values())

# @lc code=end
assert Solution().maxPointsInsideSquare([[1, -1]], "a") == 1
assert (
    Solution().maxPointsInsideSquare(points=[[1, 1], [-1, -1], [2, -2]], s="ccd") == 0
)
assert (
    Solution().maxPointsInsideSquare(points=[[1, 1], [-2, -2], [-2, 2]], s="abb") == 1
)
assert (
    Solution().maxPointsInsideSquare(
        points=[[2, 2], [-1, -2], [-4, 4], [-3, 1], [3, -3]], s="abdca"
    )
    == 2
)


#
# @lcpr case=start
# [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]]\n"abdca"\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[-2,-2],[-2,2]]\n"abb"\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[-1,-1],[2,-2]]\n"ccd"\n
# @lcpr case=end

#
