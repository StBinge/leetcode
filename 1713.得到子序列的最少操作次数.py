#
# @lc app=leetcode.cn id=1713 lang=python3
#
# [1713] 得到子序列的最少操作次数
#
from sbw import *


# @lc code=start
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        pos = {n: i for i, n in enumerate(target)}
        d = []
        for n in arr:
            if n not in pos:
                continue
            idx = pos[n]
            _idx = bisect_left(d,idx)
            if _idx < len(d):
                d[_idx] = idx
            else:
                d.append(idx)
        return len(target) - len(d)


# @lc code=end

assert Solution().minOperations(target=[5, 1, 3], arr=[9, 4, 2, 3, 4]) == 2
