#
# @lc app=leetcode.cn id=789 lang=python3
#
# [789] 逃脱阻碍者
#
from typing import List


# @lc code=start
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        steps = abs(target[0]) + abs(target[1])
        for gx, gy in ghosts:
            step = abs(gx - target[0]) + abs(gy - target[1])
            if step <= steps:
                return False
        return True


# @lc code=end
ghosts=[[1,9],[2,-5],[3,8],[9,8],[-1,3]]
target=[8,-10]
assert Solution().escapeGhosts(ghosts, target) == False

ghosts = [[1, 0], [0, 3]]
target = [0, 1]
assert Solution().escapeGhosts(ghosts, target)
ghosts = [[1, 0]]
target = [2, 0]
assert Solution().escapeGhosts(ghosts, target) == False
