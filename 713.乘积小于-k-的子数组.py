#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于 K 的子数组
#
from typing import List
# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<2:
            return 0

        ret=0
        product=1
        left=0
        for i,n in enumerate(nums):
            product*=n
            while left<=i and product>=k:
                product//=nums[left]
                left+=1
            ret+=(i-left+1)
        return ret
# @lc code=end

assert Solution().numSubarrayProductLessThanK([10,5,2,6],100)==8
assert Solution().numSubarrayProductLessThanK([10,5,2,6],0)==0