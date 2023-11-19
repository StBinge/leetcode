#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#
from typing import List
# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        bigger=-1
        small=-1
        if nums[0]>nums[1]:
            bigger=0
            small=1
        else:
            bigger=1
            small=0
        for i in range(2,len(nums)):
            n=nums[i]
            if n>nums[bigger]:
                bigger,small=i,bigger
            elif n>nums[small]:
                small=i
        return bigger if nums[bigger]>=2*nums[small] else -1
# @lc code=end
nums=[0,2,0,1]
assert Solution().dominantIndex(nums)==1

nums = [3,6,1,0]
assert Solution().dominantIndex(nums)==1
nums = [1,2,3,4]
assert Solution().dominantIndex(nums)==-1
