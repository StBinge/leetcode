#
# @lc app=leetcode.cn id=462 lang=python3
#
# [462] 最小操作次数使数组元素相等 II
#
from typing import List
# @lc code=start
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid=nums[len(nums)//2]
        return sum([abs(n-mid) for n in nums])

# @lc code=end

