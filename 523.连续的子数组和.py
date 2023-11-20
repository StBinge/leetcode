#
# @lc app=leetcode.cn id=523 lang=python3
#
# [523] 连续的子数组和
#
from typing import List
# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums)<2:
            return False
        map={0:-1}
        remainder=0
        for i in range(len(nums)):
            remainder=(remainder+nums[i])%k
            if remainder in map:
                if i-map[remainder]>=2:
                    return True
            else:
                map[remainder]=i
        return False
# @lc code=end
nums = [23,2,4,6,7]
k = 6
assert Solution().checkSubarraySum(nums,k)
nums = [23,2,6,4,7]
k = 6
assert Solution().checkSubarraySum(nums,k)

nums = [23,2,6,4,7]
k = 13
assert Solution().checkSubarraySum(nums,k)==False

