#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#
from typing import List
# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        mul1=nums[-1]*nums[-2]*nums[-3]
        mul2=nums[0]*nums[1]*nums[-1]
        return max(mul1,mul2)
# @lc code=end
assert Solution().maximumProduct([1,2,3])==6
assert Solution().maximumProduct([1,2,3,4])==24
assert Solution().maximumProduct([-1,-2,-3])==-6
