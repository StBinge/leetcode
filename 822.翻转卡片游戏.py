#
# @lc app=leetcode.cn id=822 lang=python3
#
# [822] 翻转卡片游戏
#
from typing import List
# @lc code=start
import heapq


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        invalid = set()
        ret = 3000
        for i in range(len(fronts)):
            if backs[i] == fronts[i]:
                invalid.add(backs[i])
        for f in fronts:
            if f not in invalid:
                ret = min(ret, f)
        for b in backs:
            if b not in invalid:
                ret = min(ret, b)
        return ret % 3000


# @lc code=end
fronts = [1, 2, 4, 4, 7]
backs = [1, 3, 4, 1, 3]
assert Solution().flipgame(fronts, backs) == 2
assert Solution().flipgame([1], [1]) == 0
