#
# @lc app=leetcode.cn id=1295 lang=python3
#
# [1295] 统计位数为偶数的数字
#
from sbw import *
# @lc code=start
import math
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(int(math.log10(n)+1)%2==0 for n in nums)
# @lc code=end
assert Solution().findNumbers(nums = [12,345,2,6,7896])==2
