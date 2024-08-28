#
# @lc app=leetcode.cn id=1863 lang=python3
#
# [1863] 找出所有子集的异或总和再求和
#
from sbw import *
# @lc code=start
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ret=0
        for n in nums:
            ret|=n
        return ret<<(len(nums)-1)

# @lc code=end
assert Solution().subsetXORSum([3,4,5,6,7,8])==480
assert Solution().subsetXORSum([5,1,6])==28
