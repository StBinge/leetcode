#
# @lc app=leetcode.cn id=1035 lang=python3
#
# [1035] 不相交的线
#
from sbw import *
# @lc code=start
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        L1,L2=len(nums1),len(nums2)
        f=[[0]*(L2+1) for _ in range(L1+1)]
        for i in range(1,L1+1):
            for j in range(1,L2+1):
                if nums1[i-1]==nums2[j-1]:
                    f[i][j]=f[i-1][j-1]+1
                else:
                    f[i][j]=max(f[i-1][j],f[i][j-1])
        return f[-1][-1]
    


# @lc code=end
nums1 = [1,3,7,1,7,5]
nums2 = [1,9,2,5,1]
assert Solution().maxUncrossedLines(nums1,nums2)==2

nums1 = [2,5,1,2,5]
nums2 = [10,5,2,1,5,2]
assert Solution().maxUncrossedLines(nums1,nums2)==3

nums1 = [1,4,2]
nums2 = [1,2,4]
assert Solution().maxUncrossedLines(nums1,nums2)==2
