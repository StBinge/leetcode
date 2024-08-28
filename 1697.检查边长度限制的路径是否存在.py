#
# @lc app=leetcode.cn id=1697 lang=python3
#
# [1697] 检查边长度限制的路径是否存在
#
from sbw import *


# @lc code=start
class Solution:
    def distanceLimitedPathsExist(
        self, n: int, edgeList: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        N = len(queries)
        sorted_qidx = sorted(range(N), key=lambda x: queries[x][2])

        p = list(range(n))
        size = [1] * n

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return
            if size[px] < size[py]:
                px, py = py, px
            p[py] = px
            size[px] += size[py]

        ret = [False] * N
        # used=[False]*len(edgeList)
        edgeList.sort(key=lambda x: x[2])
        idx = 0
        L = len(edgeList)
        for qidx in sorted_qidx:
            x, y, limit = queries[qidx]
            while idx < L and edgeList[idx][2] < limit:
                union(edgeList[idx][0], edgeList[idx][1])
                idx += 1
            ret[qidx] = find(x) == find(y)
        return ret


# @lc code=end
assert Solution().distanceLimitedPathsExist(
    n=5,
    edgeList=[[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]],
    queries=[[0, 4, 14], [1, 4, 13]],
) == [True, False]
assert Solution().distanceLimitedPathsExist(
    n=3,
    edgeList=[[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]],
    queries=[[0, 1, 2], [0, 2, 5]],
) == [False, True]
