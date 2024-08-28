#
# @lc app=leetcode.cn id=1748 lang=python3
#
# [1748] 唯一元素的和
#
from sbw import *
# @lc code=start
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        state={}
        ret=0
        for n in nums:
            if n not in state:
                ret+=n
                state[n]=1
            elif state[n]==1:
                ret-=n
                state[n]=2
        return ret
# @lc code=end

