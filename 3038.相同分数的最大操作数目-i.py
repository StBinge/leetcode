#
# @lc app=leetcode.cn id=3038 lang=python3
#
# [3038] 相同分数的最大操作数目 I
#
from sbw import *
# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        s=nums[0]+nums[1]
        idx=2
        L=len(nums)
        ret=1
        while idx+1<L and nums[idx]+nums[idx+1]==s:
            ret+=1
            idx+=2
        return ret
# @lc code=end
assert Solution().maxOperations([3,2,6,1,4])==1
assert Solution().maxOperations([3,2,1,4,5])==2
