#
# @lc app=leetcode.cn id=801 lang=python3
#
# [801] 使序列递增的最小交换次数
#
from typing import List
# @lc code=start
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        d0=0
        d1=1
        N=len(nums1)
        for i in range(1,N):
            _d0=d0
            _d1=d1
            d0=d1=N
            if nums1[i]>nums1[i-1] and nums2[i]>nums2[i-1]:
                d0=min(d0,_d0)
                d1=min(d1,_d1+1)
            if nums1[i]>nums2[i-1] and nums2[i]>nums1[i-1]:
                d0=min(d0,_d1)
                d1=min(d1,_d0+1)

        return min(d0,d1)

# @lc code=end
nums1 = [1,3,5,4]
nums2 = [1,2,3,7]
assert Solution().minSwap(nums1,nums2)==1
nums1 = [0,3,5,8,9]
nums2 = [2,1,4,6,9]
assert Solution().minSwap(nums1,nums2)==1