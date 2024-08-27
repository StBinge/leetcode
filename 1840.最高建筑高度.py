#
# @lc app=leetcode.cn id=1840 lang=python3
#
# [1840] 最高建筑高度
#
from sbw import *


# @lc code=start
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])

        N = len(restrictions)
        for i in range(1, N):
            pre, pre_h = restrictions[i - 1]
            cur, cur_h = restrictions[i]
            restrictions[i][1] = min(cur_h, +pre_h + cur - pre)

        for i in range(N - 2, 0, -1):
            pre, pre_h = restrictions[i + 1]
            cur, cur_h = restrictions[i]
            restrictions[i][1] = min(cur_h, pre - cur + pre_h)

        ret = 0
        for left, right in pairwise(restrictions):
            ret = max(ret, (left[1] + right[1] + right[0] - left[0]) // 2)
        return ret


# @lc code=end
assert Solution().maxBuilding(n=6, restrictions=[]) == 5
assert Solution().maxBuilding(n=5, restrictions=[[2, 1], [4, 1]]) == 2
