#
# @lc app=leetcode.cn id=974 lang=python3
#
# [974] 和可被 K 整除的子数组
#
from sbw import *
# @lc code=start
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        presum=0
        modules={0:1}
        ret=0
        for n in nums:
            presum+=n
            m=presum%k
            same=modules.get(m,0)
            ret+=same
            modules[m]=same+1
        return ret
# @lc code=end
nums=[0,-5]
k=10
assert Solution().subarraysDivByK(nums,k)==1

nums = [5]
k = 9
assert Solution().subarraysDivByK(nums,k)==0

nums = [4,5,0,-2,-3,1]
k = 5
ret=7
assert Solution().subarraysDivByK(nums,k)==ret
