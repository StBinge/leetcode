#
# @lc app=leetcode.cn id=1855 lang=python3
#
# [1855] 下标对中的最大距离
#
from sbw import *
# @lc code=start
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[-1]>nums2[0]:
            return 0
        N1,N2=len(nums1),len(nums2)
        i=j=0
        while i<N1 and j<N2:
            if nums1[i]>nums2[j]:
                i+=1
            j+=1
        return max(j-i-1,0)
# @lc code=end
assert Solution().maxDistance(nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5])==2
assert Solution().maxDistance(nums1 = [30,29,19,5], nums2 = [25,25,25,25,25])==2
assert Solution().maxDistance(nums1 = [2,2,2], nums2 = [10,10,1])==1
