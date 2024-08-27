#
# @lc app=leetcode.cn id=1719 lang=python3
#
# [1719] 重构一棵树的方案数
#
from sbw import *


# @lc code=start
class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        nodes = set()
        adj = [[False] * 501 for _ in range(501)]
        cnts = [0] * 501
        for x, y in pairs:
            cnts[x] += 1
            cnts[y] += 1
            adj[x][y] = True
            adj[y][x] = True
            nodes.add(x)
            nodes.add(y)
        N = len(nodes)
        if N - 1 > len(pairs):
            return 0
        nodes = sorted(nodes, key=cnts.__getitem__, reverse=True)
        if nodes[0]!=N-1:
            return 0
        ans = 1
        for i in range(1,N):
            ni=nodes[i]
            for j in range(i-1,-1,-1):
                nj=nodes[j]
                if adj[ni][nj]:
                    if cnts[ni]==cnts[nj]:
                        ans=2
                    break
            else:
                return 0
            for node in nodes:
                if node==nj:
                    continue
                if adj[ni][node] and not adj[nj][node]:
                    return 0
        return ans

# @lc code=end

assert Solution().checkWays([[1,3],[7,11],[11,14],[13,14],[3,14],[7,15],[3,10],[3,7],[11,12],[3,9],[7,8],[1,7],[5,6],[13,15],[6,7],[7,13],[3,6],[3,5],[5,9],[9,13],[12,14],[7,10],[8,9],[9,15],[5,14],[1,14],[6,14],[8,11],[9,12],[10,14],[4,14],[2,14],[5,7],[1,6],[2,7],[8,14],[9,14],[6,9],[14,15],[7,12],[9,10],[9,11],[1,9],[7,14],[8,12]]) == 0
assert Solution().checkWays([[1, 2], [2, 3], [2, 4], [1, 5]]) == 0
assert Solution().checkWays([[1, 2], [2, 3], [1, 3]]) == 2
assert Solution().checkWays([[1, 2], [2, 3]]) == 1
