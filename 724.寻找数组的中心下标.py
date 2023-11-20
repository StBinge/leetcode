#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心下标
#
from typing import List
# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        # for n in nums:
        #     presum_l.append(n+presum_l[-1])
        
        sum_l=0
        for i in range(len(nums)):
            if sum_l*2+nums[i]==total:
                return i
            sum_l+=nums[i]
        return -1
# @lc code=end
nums = [1, 2, 3]
assert Solution().pivotIndex(nums)==-1

nums = [1, 7, 3, 6, 5, 6]
assert Solution().pivotIndex(nums)==3