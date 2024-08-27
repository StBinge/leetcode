#
# @lc app=leetcode.cn id=1743 lang=python3
#
# [1743] 从相邻元素对还原数组
#
from sbw import *


# @lc code=start
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for x, y in adjacentPairs:
            adj[x].append(y)
            adj[y].append(x)
        ret = []
        for k in adj:
            if len(adj[k]) == 1:
                ret.append(k)
                break

        ret.append(adj[ret[-1]][0])
        for i in range(len(adjacentPairs) - 1):
            x, y = adj[ret[-1]]
            if x==ret[-2]:
                x=y
            ret.append(x)
        return ret


# @lc code=end
ret = Solution().restoreArray([[4,-2],[1,4],[-3,1]])
ans = [-2,4,1,-3]
assert ret == ans or ret == ans[::-1]
ret = Solution().restoreArray(adjacentPairs=[[2, 1], [3, 4], [3, 2]])
ans = [1, 2, 3, 4]
assert ret == ans or ret == ans[::-1]
