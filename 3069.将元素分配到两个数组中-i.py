#
# @lc app=leetcode.cn id=3069 lang=python3
#
# [3069] 将元素分配到两个数组中 I
#
from sbw import *
# @lc code=start
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        ret1=[nums[0]]
        ret2=[nums[1]]
        for n in nums[2:]:
            if ret1[-1]>ret2[-1]:
                ret1.append(n)
            else:
                ret2.append(n)
        return ret1+ret2

# @lc code=end

