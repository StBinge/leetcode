#
# @lc app=leetcode.cn id=1283 lang=python3
#
# [1283] 使结果不超过阈值的最小除数
#
from sbw import *
# @lc code=start
import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # mi,ma=10**7,0
        # for n in nums:
        #     mi=min(mi,n)
        #     ma=max(ma,n)
        # L=len(nums)
        # mi=nums[0]
        left=1
        right=max(nums)+1
        while left<right:
            mid=(left+right)//2
            s=sum((n-1)//mid+1 for n in nums)
            if s>threshold:
                left=mid+1
            else:
                right=mid
        return right
# @lc code=end
assert Solution().smallestDivisor(nums = [19], threshold = 5)==4
assert Solution().smallestDivisor(nums = [2,3,5,7,11], threshold = 11)==3
assert Solution().smallestDivisor(nums = [1,2,5,9], threshold = 6)==5
