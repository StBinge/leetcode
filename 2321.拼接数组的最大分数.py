#
# @lc app=leetcode.cn id=2321 lang=python3
#
# [2321] 拼接数组的最大分数
#
from sbw import *
# @lc code=start
class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        # L=len(nums1)
        s1=sum(nums1)
        s2=sum(nums2)
        def max_dif(n1,n2):
            max_d=0
            d=0
            for x,y in zip(n1,n2):
                d+=x-y
                if d<0:
                    d=0
                max_d=max(max_d,d)
            return max_d

        return max(s2+max_dif(nums1,nums2),s1+max_dif(nums2,nums1))
# @lc code=end
assert Solution().maximumsSplicedArray([10,20,50,15,30,10],[40,20,10,100,10,10])==230
assert Solution().maximumsSplicedArray(nums1 = [7,11,13], nums2 = [1,1,1])==31
assert Solution().maximumsSplicedArray(nums1 = [20,40,20,70,30], nums2 = [50,20,50,40,20])==220
assert Solution().maximumsSplicedArray(nums1 = [60,60,60], nums2 = [10,90,10])==210
