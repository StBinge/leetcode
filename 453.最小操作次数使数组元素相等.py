#
# @lc app=leetcode.cn id=453 lang=python3
#
# [453] 最小操作次数使数组元素相等
#
from typing import List
# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        Min=min(nums)
        return sum(nums)-Min*len(nums)

# @lc code=end

assert Solution().minMoves([1,2,3])==3
assert Solution().minMoves([1,1,1])==0