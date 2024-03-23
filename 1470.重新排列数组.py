#
# @lc app=leetcode.cn id=1470 lang=python3
#
# [1470] 重新排列数组
#
from sbw import *
# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ret=[0]*(n*2)

        for i in range(0,n*2,2):
            ret[i]=nums[i//2]
            ret[i+1]=nums[i//2+n]
        return ret
# @lc code=end

assert Solution().shuffle(nums = [2,5,1,3,4,7], n = 3)==[2,3,5,4,1,7] 