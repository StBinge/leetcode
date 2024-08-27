#
# @lc app=leetcode.cn id=1785 lang=python3
#
# [1785] 构成特定和需要添加的最少元素
#
from sbw import *


# @lc code=start
class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        s = sum(nums)
        dif = abs(goal - s)
        return (dif - 1) // limit + 1


# @lc code=end
assert Solution().minElements(nums=[1, -10, 9, 1], limit=100, goal=0) == 1
assert Solution().minElements(nums=[1, -1, 1], limit=3, goal=-4) == 2
