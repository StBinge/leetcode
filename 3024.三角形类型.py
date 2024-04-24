#
# @lc app=leetcode.cn id=3024 lang=python3
#
# [3024] 三角形类型
#
from sbw import *


# @lc code=start
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        x, y, z = nums
        if x + y <= z:
            return "none"
        if x == z:
            return "equilateral"
        if x == y or y == z:
            return "isosceles"
        return "scalene"


# @lc code=end
assert Solution().triangleType([8,4,4]) == "none"
assert Solution().triangleType([3, 3, 3]) == "equilateral"
