#
# @lc app=leetcode.cn id=1458 lang=python3
#
# [1458] 两个子序列的最大点积
#
from sbw import *
# @lc code=start
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        l1,l2=len(nums1),len(nums2)
        f=[[0] * l2 for _ in range(l1)]
        f[0][0]=nums1[0]*nums2[0]
        for i in range(1,l1):
            f[i][0]=max(nums1[i]*nums2[0],f[i-1][0])
        for j in range(1,l2):
            f[0][j]=max(nums1[0]*nums2[j],f[0][j-1])

        for i in range(1,l1):
            for j in range(1,l2):
                xij=nums1[i]*nums2[j]
                f[i][j]=max(xij,f[i-1][j-1]+xij,f[i-1][j],f[i][j-1])
        return f[-1][-1]


# @lc code=end
assert Solution().maxDotProduct(nums1 = [2,1,-2,5], nums2 = [3,0,-6])==18
assert Solution().maxDotProduct(nums1 = [-1,-1], nums2 = [1,1])==-1
assert Solution().maxDotProduct(nums1 = [3,-2], nums2 = [2,-6,7])==21
