#
# @lc app=leetcode.cn id=915 lang=python3
#
# [915] 分割数组
#
import enum
from sbw import *
# @lc code=start
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        l=len(nums)
        cur_max=left_max=nums[0]
        pos=0
        for i in range(1,l):
            cur_max=max(cur_max,nums[i])
            if nums[i]<left_max:
                left_max,pos=cur_max,i
        return pos+1
# @lc code=end
nums = [1,1,1,0,6,12]
assert Solution().partitionDisjoint(nums)==4

nums = [5,0,3,8,6]
assert Solution().partitionDisjoint(nums)==3
